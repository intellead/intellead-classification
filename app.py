# -*- coding: utf-8 -*-


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
    send_data_to_connector(json_lead['lead'], lead_status)
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
    data['lead_status'] = lead_status['value']
    data['lead_status_proba'] = lead_status['proba']
    leads = {}
    leads['leads'] = [data]
    url = os.getenv('CONNECTOR_CLASSIFICATION_WEBHOOK', 'http://intellead-connector:3000/intellead-webhook')
    r = requests.post(url, json=leads)
    print('The lead ' + data['email'] + ' was sent to intellead-connector with status code: ' + str(r.status_code))


if __name__ == '__main__':
    app.run(host='0.0.0.0')




