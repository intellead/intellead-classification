import requests
import json
from flask import Flask, abort

import normalize
import service

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/lead_status/<int:lead_id>', methods=['GET'])
def get_lead_status(lead_id):
    lead = get_data_from_lead(lead_id)
    if lead == None:
        abort(404)
    data_from_lead = normalize.data(lead)
    lead_status = service.classification(data_from_lead)
    return lead_status


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




