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


def classification(lead):
    #classifiers = [
    #    ('ab', AdaBoostClassifier()),
    #    ('dt', DecisionTreeClassifier(max_depth=5)),
    #    ('kn', KNeighborsClassifier(16)),
    #]
    inputs = get_dataset_input_from_database(lead.keys())
    outputs = get_dataset_output_from_database()
    print('The total number of examples in the dataset is: %d' % (len(inputs)))
    inputs_training, inputs_test, outputs_training, outputs_test = train_test_split(inputs, outputs, test_size=0.3, random_state=42)
    print('The number of examples used for training are: %d' % (len(inputs_training)))
    print('The number of examples used for testing are: %d' % (len(inputs_test)))
    knn = KNeighborsClassifier(n_neighbors=7, p=2)
    knn.fit(inputs_training, np.ravel(outputs_training))
    print('[K=7] The probability of the algorithm to be right is: %f%%' % (knn.score(inputs_test, outputs_test) * 100))
    #voting_classifier = VotingClassifier(estimators=classifiers, voting='hard')
    #voting_classifier = voting_classifier.fit(inputs_training, np.ravel(outputs_training))
    #print('The probability of the machine to be right is: %f%%' % (voting_classifier.score(inputs_test, outputs_test) * 100))
    print('Lead data:')
    print(lead)
    data_to_predict = convert_dict_to_tuple(lead)
    print('Lead data to predict:')
    print(data_to_predict)
    lead_status = knn.predict(data_to_predict)
    lead_status_value = lead_status[0]
    #lead_status = voting_classifier.predict(data_to_predict)
    print('According to lead data, his status is: %d' % (lead_status_value))
    print('[0] unqualified [1] qualified')
    proba = knn.predict_proba(data_to_predict)
    max_proba = max(proba[0])
    print('Proba is: %d%%' %(max_proba*100))
    lead_status_dict = dict()
    dict.update(lead_status_dict, value=str(lead_status_value))
    dict.update(lead_status_dict, proba=str(max_proba))
    return lead_status_dict


def convert_dict_to_tuple(data):
    data_tuple = (data['role'], data['profile'], data['conversion'], data['lead_area'], data['number_of_employees'], data['company_segment'], data['wip'], data['source_first_conv'], data['source_last_conv'], data['concern'], data['looking_for_a_software'])
    if 'main_activity' in data.keys():
        data_tuple = data_tuple + (data['main_activity'],)
    return data_tuple


def save_lead_in_dataset(data):
    try:
        columns = ['email', 'job_title', 'lead_profile', 'conversions', 'area', 'number_employees', 'segment', 'work_in_progress', 'source_first_conversion', 'source_last_conversion', 'concern', 'looking_for_management_software']
        if 'main_activity' in data.keys():
            columns.append('cnae')
        values = ((data['email'],) + convert_dict_to_tuple(data))
        insert_statement = 'insert into dataset (%s) values %s'
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_dataset_input_from_database(fields):
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
        if 'main_activity' in fields:
            cur.execute('SELECT job_title, lead_profile, conversions, area, number_employees, segment, work_in_progress, source_first_conversion, source_last_conversion, concern, looking_for_management_software, cnae FROM dataset')
        else:
            cur.execute('SELECT job_title, lead_profile, conversions, area, number_employees, segment, work_in_progress, source_first_conversion, source_last_conversion, concern, looking_for_management_software FROM dataset')
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return np.array(rows)


def get_dataset_output_from_database():
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT lead_status FROM dataset')
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return np.array(rows)


def get_connection():
    try:
        conn = psycopg2.connect(host=os.getenv('DATABASE_HOST', 'intellead-classification-postgresql'), database=os.getenv('DATABASE_NAME', 'postgres'),
                                user=os.getenv('DATABASE_USER', 'postgres'), password=os.getenv('DATABASE_PASSWORD', 'postgres'))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn
