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

from classification_algorithm import ClassificationAlgorithm
from sklearn.model_selection import train_test_split
import numpy as np
import psycopg2
from psycopg2.extensions import AsIs
import os
from boto.s3.connection import S3Connection


s3 = S3Connection(os.getenv('DATABASE_NAME', 'postgres'), os.getenv('DATABASE_USER', 'postgres'), os.getenv('DATABASE_PASSWORD', 'postgres'), os.getenv('DATABASE_HOST', 'intellead-classification-postgresql'), os.getenv('DATABASE_PORT', 5432))


def classification(customer, lead):
    try:
        inputs = get_dataset_input_from_database(customer)
        outputs = get_dataset_output_from_database(customer)
        algorithm = get_algorithm(customer)
        print('Examples in dataset is: %d' % (len(inputs)))
        inputs_training, inputs_test, outputs_training, outputs_test = train_test_split(inputs, outputs, test_size=0.2, random_state=42)
        print('Examples used for training is: %d' % (len(inputs_training)))
        print('Examples used for testing is: %d' % (len(inputs_test)))
        clf = algorithm
        clf.fit(inputs_training, outputs_training)
        print('Score Trainning: %f%%' % (clf.score(inputs_training, outputs_training) * 100))
        print('Score Test: %f%%' % (clf.score(inputs_test, outputs_test) * 100))
        print('Lead data:')
        print(lead)
        data_to_predict = convert_dict_to_tuple(lead, customer)
        print('Lead data to predict:')
        print(data_to_predict)
        lead_status = clf.predict(data_to_predict)
        lead_status_value = lead_status[0]
        proba = clf.predict_proba(data_to_predict)
        max_proba = max(proba[0])
        print('According to lead data, his status is: %s' % ("QUALIFICADO" if lead_status_value == 1 else "NÃO QUALIFICADO"))
        print('Proba is: %d%%' % (max_proba*100))
        lead_status_dict = dict()
        dict.update(lead_status_dict, value=str(lead_status_value))
        dict.update(lead_status_dict, proba=str(max_proba))
        return lead_status_dict
    except Exception as ex:
        print(ex)



def get_dataset_input_from_database(customer):
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     example_value.value '
                    ' FROM '
                    '     example_values example_value '
                    '     INNER JOIN examples example ON example.id = example_value.example_id '
                    '     INNER JOIN fields field ON example_value.field_id = field.id '
                    ' WHERE '
                    '     example.customer = %s '
                    '     AND field.type = \'input\' '
                    '     AND field.customer = %s '
                    ' ORDER BY '
                    '     example_value.example_id , '
                    '     field.name ', [customer, customer])
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
                    '     INNER JOIN examples example ON example.id = example_value.example_id '
                    '     INNER JOIN fields field ON example_value.field_id = field.id '
                    ' WHERE '
                    '     example.customer = %s '
                    '     AND field.type = \'output\' '
                    '     AND field.customer = %s ', [customer, customer])
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


def get_algorithm(customer):
    algorithm = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(' SELECT '
                    '     algorithm '
                    ' FROM '
                    '     customer_config '
                    ' WHERE '
                    '     customer = %s ', [customer])
        algorithm = cur.fetchone()[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            if algorithm is not None:
                print(algorithm)
                return ClassificationAlgorithm[algorithm].value
            return ClassificationAlgorithm.KNN.value


def get_connection():
    try:
        conn = psycopg2.connect(host=os.getenv('DATABASE_HOST', 'intellead-classification-postgresql'), database=os.getenv('DATABASE_NAME', 'postgres'),
                                user=os.getenv('DATABASE_USER', 'postgres'), password=os.getenv('DATABASE_PASSWORD', 'postgres'))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn
