import requests
import json
import psycopg2
import os
from boto.s3.connection import S3Connection
from flask import Flask, abort

import normalize
import service

app = Flask(__name__)

s3 = S3Connection(os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'], os.environ['DATABASE_PASSWORD'], os.environ['DATABASE_HOST'], os.environ['DATABASE_PORT'])

@app.route('/')
def index():
    return "Intellead Classification"


@app.route('/lead_status/<int:lead_id>', methods=['GET'])
def get_lead_status(lead_id):
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=os.environ.get('DATABASE_HOST'), database=os.environ.get('DATABASE_NAME'), user=os.environ.get('DATABASE_USER'), password=os.environ.get('DATABASE_PASSWORD'))
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    json_lead = get_data_from_lead(lead_id)
    if (json_lead is None) | (json_lead == ''):
        abort(404)
    normalized_data = normalize.lead(json_lead)
    lead_status = service.classification(normalized_data)
    return str(lead_status)


def get_data_from_lead(lead_id):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
    }
    url = 'https://intellead-data.herokuapp.com/lead-info';
    data = {"lead_id": str(lead_id)}
    response = requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)




