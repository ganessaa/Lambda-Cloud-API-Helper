'''Wrapper for Lambda Cloud API
'''

import requests
import libs.env as env
import json

URL_BASE = 'https://cloud.lambdalabs.com/api/v1/'
HEADER = {
    'Content-Type': 'application/json',
}


def get(api):
    res = requests.get(
        ''.join([URL_BASE, api]),
        headers=HEADER,
        auth=(env.API_KEY, ''),
    )
    return res.json()


def post(api, data):
    res = requests.post(
        ''.join([URL_BASE, api]),
        headers=HEADER,
        data=json.dumps(data),
        auth=(env.API_KEY, ''),
    )
    return res.json()
