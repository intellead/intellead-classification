from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
import numpy as np
import psycopg2
import os
from boto.s3.connection import S3Connection


s3 = S3Connection(os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'], os.environ['DATABASE_PASSWORD'], os.environ['DATABASE_HOST'], os.environ['DATABASE_PORT'])


def classification(lead):
    classifiers = [
        ('ab', AdaBoostClassifier()),
        ('dt', DecisionTreeClassifier(max_depth=5)),
        ('kn', KNeighborsClassifier(16)),
    ]
    inputs = get_dataset_input_from_database(lead.keys())
    outputs = get_dataset_output_from_database()
    print('The total number of examples in the dataset is: %d' % (len(inputs)))
    inputs_training, inputs_test, outputs_training, outputs_test = train_test_split(inputs, outputs, test_size=0.3, random_state=42)
    print('The number of examples used for training are: %d' % (len(inputs_training)))
    print('The number of examples used for testing are: %d' % (len(inputs_test)))
    voting_classifier = VotingClassifier(estimators=classifiers, voting='hard')
    voting_classifier = voting_classifier.fit(inputs_training, np.ravel(outputs_training))
    print('The probability of the machine to be right is: %f%%' % (voting_classifier.score(inputs_test, outputs_test) * 100))
    print('Lead data:')
    print(lead)
    data_to_predict = convert_dict_to_tuple(lead)
    print('Lead data to predict:')
    print(data_to_predict)
    lead_status = voting_classifier.predict(data_to_predict)
    print('According to lead data, his status is: %d' % (lead_status))
    print('[0] unqualified [1] qualified')
    return lead_status


def convert_dict_to_tuple(data):
    data_tuple = (data['role'], data['profile'], data['conversion'], data['lead_area'], data['number_of_employees'], data['company_segment'], data['wip'], data['source_first_conv'], data['source_last_conv'], data['concern'], data['looking_for_a_software'])
    if 'main_activity' in data.keys():
        data_tuple = data_tuple + (data['main_activity'],)
    return data_tuple


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
        conn = psycopg2.connect(host=os.environ.get('DATABASE_HOST'), database=os.environ.get('DATABASE_NAME'),
                                user=os.environ.get('DATABASE_USER'), password=os.environ.get('DATABASE_PASSWORD'))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn