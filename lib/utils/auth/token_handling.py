import requests
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def request_token(token_params):
    token_data = None
    url = 'https://www.strava.com/api/v3/oauth/token'
    body = {
        'client_id': token_params['CLIENT_ID'],
        'client_secret': token_params['CLIENT_SECRET'],
        'refresh_token': token_params['REFRESH_TOKEN'],
        'grant_type': 'refresh_token'
    }
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(body), headers=headers)

    request_status = r.status_code
    if request_status == 200:
        token_data = r.json()
    else:
        logger.error(request_status)

    return token_data
