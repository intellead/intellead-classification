# Copyright 2017 Softplan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import psycopg2
from psycopg2.extensions import AsIs
import os
from boto.s3.connection import S3Connection


s3 = S3Connection(os.getenv('DATABASE_NAME', 'postgres'), os.getenv('DATABASE_USER', 'postgres'), os.getenv('DATABASE_PASSWORD', 'postgres'), os.getenv('DATABASE_HOST', 'intellead-classification-postgresql'), os.getenv('DATABASE_PORT', 5432))


def classification(customer, lead):
    inputs = get_dataset_input_from_database(customer)
    outputs = get_dataset_output_from_database(customer)
    print('The total number of examples in the dataset is: %d' % (len(inputs)))
    inputs_training, inputs_test, outputs_training, outputs_test = train_test_split(inputs, outputs, test_size=0.3, random_state=42)
    print('The number of examples used for training are: %d' % (len(inputs_training)))
    print('The number of examples used for testing are: %d' % (len(inputs_test)))
    knn = KNeighborsClassifier(n_neighbors=7, p=2)
    knn.fit(inputs_training, np.ravel(outputs_training))
    print('[K=7] The probability of the algorithm to be right is: %f%%' % (knn.score(inputs_test, outputs_test) * 100))
    print('Lead data:')
    print(lead)
    data_to_predict = convert_dict_to_tuple(lead, customer)
    print('Lead data to predict:')
    print(data_to_predict)
    lead_status = knn.predict(data_to_predict)
    lead_status_value = lead_status[0]
    print('According to lead data, his status is: %s' % (lead_status_value))
    print('[0] unqualified [1] qualified')
    proba = knn.predict_proba(data_to_predict)
    max_proba = max(proba[0])
    print('Proba is: %d%%' %(max_proba*100))
    lead_status_dict = dict()
    dict.update(lead_status_dict, value=str(lead_status_value))
    dict.update(lead_status_dict, proba=str(max_proba))
    return lead_status_dict


def get_dataset_input_from_database(customer):
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     example_value.value '
                    ' FROM '
                    '     example_values example_value '
                    '     INNER JOIN fields field ON example_value.field_id = field.id '
                    ' WHERE '
                    '     field.type = \'input\' '
                    '     AND field.customer = %s '
                    ' ORDER BY '
                    '     example_value.example_id , '
                    '     field.name ', [customer])
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return join_rows(customer, rows)


def join_rows(customer, rows):
    fields = count_fields(customer)
    examples = count_examples(customer)
    rows_array = np.array(rows)
    joined = [[0 for x in range(fields)] for y in range(examples)]
    for index, row in enumerate(rows_array):
        field = index % fields
        example = index // fields
        joined[example][field] = row[0]
    return joined


def count_fields(customer):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     COUNT(*) '
                    ' FROM '
                    '     fields field '
                    ' WHERE '
                    '     field.type = \'input\' '
                    '     AND field.customer = %s ', [customer])
        count = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return count[0]


def count_examples(customer):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     COUNT(*) '
                    ' FROM '
                    '     examples example '
                    ' WHERE '
                    '     example.customer = %s ', [customer])
        count = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return count[0]


def get_dataset_output_from_database(customer):
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     example_value.value '
                    ' FROM '
                    '     example_values example_value '
                    '     INNER JOIN fields field ON example_value.field_id = field.id '
                    ' WHERE '
                    '     field.type = \'output\' '
                    '     AND field.customer = %s ', [customer])
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return np.array(rows)


def save_lead_in_dataset(data, customer):
    example_id = max_example_id() + 1
    example_value_id = max_example_value_id() + 1
    save_example_in_dataset(example_id, customer)
    try:
        fields = get_customer_fields(customer)
        inserts = []
        for column in fields:
            id = example_value_id
            example_value_id += 1
            field_id = int(column[1])
            value = str(data[column[0]])
            insert = (id, example_id, field_id, value)
            inserts.append(insert)

        inserts.append((example_value_id, example_id, get_customer_output_field(customer), '1'))
        inserts.append((example_value_id, example_id, get_customer_email_field(customer), data['email']))

        conn = get_connection()
        cur = conn.cursor()
        for insert in inserts:
            cur.execute('insert into example_values (id, example_id, field_id, value) values %s', (insert,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def save_example_in_dataset(example_id, customer):
    try:
        columns = ['id', 'customer']
        values = (example_id, customer)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('insert into examples (%s) values %s', (AsIs(','.join(columns)), tuple(values)))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def max_example_id():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     MAX(example.id) '
                    ' FROM '
                    '     examples example ')
        max = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return max[0]


def max_example_value_id():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     MAX(example_value.id) '
                    ' FROM '
                    '     example_values example_value ')
        max = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return max[0]


def convert_dict_to_tuple(data, customer):
    tup = ()
    for index, row in enumerate(get_customer_fields(customer)):
        tup += (data[row[0]],)
    return tup


def get_customer_fields(customer):
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     field.name, '
                    '     field.id '
                    ' FROM '
                    '     fields field '
                    ' WHERE '
                    '     field.type = \'input\' '
                    '     AND field.customer = %s '
                    ' ORDER BY '
                    '     field.name ', [customer])
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return np.array(rows)


def get_customer_output_field(customer):
    id = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     field.id '
                    ' FROM '
                    '     fields field '
                    ' WHERE '
                    '     field.type = \'output\' '
                    '     AND field.customer = %s '
                    ' ORDER BY '
                    '     field.name ', [customer])
        id = cur.fetchone()[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return id


def get_customer_email_field(customer):
    id = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     field.id '
                    ' FROM '
                    '     fields field '
                    ' WHERE '
                    '     field.type = \'id\' '
                    '     AND field.customer = %s '
                    '     AND field.name = \'email\' '
                    ' ORDER BY '
                    '     field.name ', [customer])
        id = cur.fetchone()[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return id


def get_connection():
    try:
        conn = psycopg2.connect(host=os.getenv('DATABASE_HOST', 'intellead-classification-postgresql'), database=os.getenv('DATABASE_NAME', 'postgres'),
                                user=os.getenv('DATABASE_USER', 'postgres'), password=os.getenv('DATABASE_PASSWORD', 'postgres'))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn
