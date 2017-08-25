# -*- coding: utf-8 -*-
import requests
import json
from flask import Flask, abort, request

import normalize
import service

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
    if lead_status == 1:
        print('1')
        teste = json.loads(json_lead)
        print('2')
        teste['lead']['lead_status'] = lead_status
        print('3')
        print(type(json.dumps(teste)))
        print('A')
        print(type(json_lead))
        print('B')
        print(type(json.dumps(json_lead)))
        print('C')

        send_data_to_connector(json_lead['lead'])
        print('connected')
    return str(lead_status)


def get_data_from_lead(lead_id):
    headers = {
        'content-type': 'application/json',
        'cache-control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
    }
    url = 'https://intellead-data.herokuapp.com/lead-info'
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
    url = 'https://intellead-data.herokuapp.com/save-lead-status'
    data = {"lead_id": str(lead_id), "lead_status": int(lead_status)}
    requests.post(url, data=json.dumps(data), json={'lead_id': str(lead_id)}, headers=headers)
    print('lead has been sended to intellead-data')


def send_data_to_connector(data):
    print(type(data))
    print(data['email'] + ' connecting... to intellead-connector')
    leads = {}
    leads['leads'] = [data]
    #print(leads)
    #print(type(leads))
    url = 'https://intellead-connector.herokuapp.com/teste'
    r = requests.post(url, json=leads)
    print(r.status_code)



if __name__ == '__main__':
    app.run(debug=True)




