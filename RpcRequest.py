import json

import requests

from constant import Constant


def post(path, method, params):
    data = create_request(method, params)
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", Constant.IMT_LOGIN_URL + '/' + path, data=json.dumps(data), headers=headers)
    return response


def create_request(method, params):
    request = {
        'id': Constant.REQUEST_ID,
        'jsonrpc': '2.0',
        'method': method,
        'params': params
    }
    return request
