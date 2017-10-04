# -*- coding: utf-8 -*-
import requests
import json
from flask import Flask, abort, request

import normalize
import service
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Intellead Classification"


@app.route('/lead_status_by_id/<int:lead_id>', methods=['GET'])
def get_lead_status_by_id(lead_id):
    json_lead = get_data_from_lead(lead_id)
    if (json_lead is None) | (json_lead == ''):
        abort(404)
    normalized_data = normalize.lead(json_lead)
    lead_status = service.classification(normalized_data)
    save_lead_status(lead_id, lead_status)
    #send_data_to_connector(json_lead['lead'], int(lead_status))
    return str(lead_status['value'])


def get_data_from_lead(lead_id):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
    }
    url = os.getenv('DATA_LEAD_INFO_URL', 'http://intellead-data:3000/lead-info')
    data = {"lead_id": str(lead_id)}
    response = requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def save_lead_status(lead_id, lead_status):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
    }
    url = os.getenv('DATA_SAVE_LEAD_STATUS_URL', 'http://intellead-data:3000/save-lead-status')
    data = {"lead_id": str(lead_id), "lead_status": lead_status}
    print(data)
    requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    print('The lead was sent to intellead-data')


def send_data_to_connector(data, lead_status):
    data['lead_status'] = int(lead_status)
    leads = {}
    leads['leads'] = [data]
    url = os.environ['CONNECTOR_CLASSIFICATION_WEBHOOK']
    r = requests.post(url, json=leads)
    print('The lead ' + data['email'] + ' was sent to intellead-connector with status code: ' + r.status_code)


if __name__ == '__main__':
    app.run(debug=True)




