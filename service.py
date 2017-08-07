from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import psycopg2
import os
from boto.s3.connection import S3Connection


s3 = S3Connection(os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'], os.environ['DATABASE_PASSWORD'], os.environ['DATABASE_HOST'], os.environ['DATABASE_PORT'])


def classification(data_from_lead):
    number_of_fields = len(data_from_lead)
    inputs = get_dataset_input_from_database()
    outputs = get_dataset_output_from_database()
    print('The total number of examples in the dataset is: %d' % (len(inputs)))
    inputs_training, inputs_test, outputs_training, outputs_test = train_test_split(inputs, outputs, test_size=0.3, random_state=42)
    print('The number of examples used for training are: %d' % (len(inputs_training)))
    print('The number of examples used for testing are: %d' % (len(inputs_test)))
    if number_of_fields == 11:
        knn = KNeighborsClassifier(n_neighbors=7, p=2)
        knn.fit(inputs_training, outputs_training)
        print('[K=7] The probability of the algorithm to be right is: %f%%' % (knn.score(inputs_test, outputs_test) * 100))
    else:
        knn = KNeighborsClassifier(n_neighbors=16, p=2)
        knn.fit(inputs_training, outputs_training)
        print('[K=16] The probability of the algorithm to be right is: %f%%' % (knn.score(inputs_test, outputs_test) * 100))
    print('Lead data:')
    print(data_from_lead)
    lead_status = knn.predict(data_from_lead)
    print('According to lead data, his status is: %d' % (lead_status))
    print('[0] unqualified [1] qualified')
    return lead_status


def get_dataset_input_from_database(number_of_fields):
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
        if number_of_fields == 11:
            cur.execute('SELECT job_title, lead_profile, conversions, area, number_employees, segment, work_in_progress, source_first_conversion, source_last_conversion, concern, looking_for_management_software FROM dataset')
        else:
            cur.execute('SELECT job_title, lead_profile, conversions, area, number_employees, segment, work_in_progress, source_first_conversion, source_last_conversion, concern, looking_for_management_software, cnae FROM dataset')
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