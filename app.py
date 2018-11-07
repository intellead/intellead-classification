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
import service
import os
from flask import Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/lead_status_by_id/<int:lead_id>', methods=['GET'])
def get_lead_status_by_id(lead_id):
    url = os.getenv('SECURITY_URL', 'http://intellead-security:8080/auth')
    token = request.headers.get('token')
    security_response = requests.post(url + '/' + str(token))
    if security_response.status_code != 200:
        abort(401)
    json_lead = get_data_from_lead(token, lead_id)
    if (json_lead is None) | (json_lead == ''):
        abort(404)
    normalized_data = normalize_lead_data(token, json_lead)
    if (normalized_data is None) | (normalized_data == ''):
        abort(404)
    security_response_json = security_response.json()
    lead_status = service.classification(security_response_json['id'], normalized_data)
    print('Classified')
    save_lead_status(token, lead_id, lead_status)
    print('Lead status saved')
    send_data_to_connector(token, json_lead['lead'], lead_status)
    print('Data sent to connector')
    return str(lead_status['value'])


@app.route('/save_lead_in_dataset', methods=['POST'])
def save_lead_in_dataset():
    url = os.getenv('SECURITY_URL', 'http://intellead-security:8080/auth')
    token = request.headers.get('token')
    security_response = requests.post(url + '/' + str(token))
    if security_response.status_code != 200:
        abort(401)
    normalized_data = request.get_json()
    if (normalized_data is None) | (normalized_data == ''):
        abort(412)
    security_response_json = security_response.json()
    service.save_lead_in_dataset(normalized_data, security_response_json['id'])
    return Response(status=201)


@app.route('/demo', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*', headers=['Content-Type', 'Accept', 'token'])
def demo():
    url = os.getenv('SECURITY_URL', 'http://intellead-security:8080/auth')
    token = request.headers.get('token')
    security_response = requests.post(url + '/' + str(token))
    if security_response.status_code != 200:
        abort(401)
    json_lead = request.get_json()
    if (json_lead is None) | (json_lead == ''):
        abort(412)
    normalized_data = normalize_lead_data(token, json_lead)
    if (normalized_data is None) | (normalized_data == ''):
        abort(500)
    security_response_json = security_response.json()
    lead_status = service.classification(security_response_json['id'], normalized_data)
    return json.dumps(lead_status)


def get_data_from_lead(token, lead_id):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36',
        'token': token
    }
    url = os.getenv('DATA_LEAD_INFO_URL', 'http://intellead-data:3000/lead-info')
    data = {"lead_id": str(lead_id)}
    response = requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def save_lead_status(token, lead_id, lead_status):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36',
        'token': token
    }
    url = os.getenv('DATA_SAVE_LEAD_STATUS_URL', 'http://intellead-data:3000/save-lead-status')
    data = {"lead_id": str(lead_id), "lead_status": lead_status}
    print(data)
    requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    print('The lead was sent to intellead-data')


def send_data_to_connector(token, data, lead_status):
    headers = {
        'token': token
    }
    data['lead_status'] = lead_status['value']
    data['lead_status_proba'] = lead_status['proba']
    leads = {}
    leads['leads'] = [data]
    url = os.getenv('CONNECTOR_CLASSIFICATION_WEBHOOK', 'http://intellead-connector:3000/intellead-webhook')
    r = requests.post(url, json=leads, headers=headers)
    print('The lead ' + data['_id'] + ' was sent to intellead-connector with status code: ' + str(r.status_code))


def normalize_lead_data(token, data):
    headers = {
        'token': token
    }
    url = os.getenv('NORMALIZATION_URL', 'http://intellead-normalization:3000/normalize')
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        normalized_data = response.json()
        print(normalized_data)
        return normalized_data
    else:
        return None


if __name__ == '__main__':
    app.run(host='0.0.0.0')




