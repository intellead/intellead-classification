from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import psycopg2
import os
from boto.s3.connection import S3Connection


s3 = S3Connection(os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'], os.environ['DATABASE_PASSWORD'], os.environ['DATABASE_HOST'], os.environ['DATABASE_PORT'])


def classification(data_from_lead):
    dataset = get_dataset_from_database()
    print('return dataset')
    x = get_dataset_input_from_database()
    print('return input dataset')
    y = get_dataset_output_from_database()
    print('return output dataset')
    # x são as entradas e y são as saídas
    #dataset1
    #x = np.genfromtxt('dataset.csv', delimiter=';', usecols=(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    #y = np.genfromtxt('dataset.csv', delimiter=';', usecols=(22))
    #dataset2
    #x = np.genfromtxt('dataset.csv', delimiter=';', usecols=(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    #y = np.genfromtxt('dataset.csv', delimiter=';', usecols=(14))
    print('The total number of examples in the dataset is: %d' % (len(x)))
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=42)
    print('The number of examples used for training are: %d' % (len(x_treino)))
    print('The number of examples used for testing are: %d' % (len(x_teste)))
    knn = KNeighborsClassifier(n_neighbors=7, p=2)
    knn.fit(x_treino, y_treino)
    print('The probability of the algorithm to be right is: %f%%' % (knn.score(x_teste, y_teste) * 100))
    print('Lead data:')
    print(data_from_lead)
    lead_status = knn.predict(data_from_lead)
    print('[0] unqualified\n[1] qualified')
    print('According to the lead data, his status is: %d' % (lead_status))
    return lead_status


def get_dataset_from_database():
    rows = [];
    try:
        print('Connecting to the PostgreSQL database...')
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM dataset')
        rows = cur.fetchall()
        print("The number of rows: ", cur.rowcount)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return rows


def get_dataset_input_from_database():
    rows = [];
    try:
        conn = get_connection()
        cur = conn.cursor()
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