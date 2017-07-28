import requests
import json
from flask import Flask, abort

import normalize
import service

app = Flask(__name__)


@app.route('/')
def index():
    return "Intellead Classification"

@app.route('/lead_status_by_id/<int:lead_id>', methods=['GET'])
def get_lead_status(lead):
    json_lead = lead
    if (json_lead is None) | (json_lead == ''):
        abort(404)
    normalized_data = normalize.lead(json_lead)
    lead_status = service.classification(normalized_data)
    return str(lead_status)

@app.route('/lead_status_by_id/<int:lead_id>', methods=['GET'])
def get_lead_status_by_id(lead_id):
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




