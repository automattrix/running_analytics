import requests
import json


def request_token(token_params):
    url = 'https://www.strava.com/api/v3/oauth/token'
    body = {
        'client_id': token_params['CLIENT_ID'],
        'client_secret': token_params['CLIENT_SECRET'],
        'refresh_token': token_params['REFRESH_TOKEN'],
        'grant_type': 'refresh_token'
    }
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r.json())
