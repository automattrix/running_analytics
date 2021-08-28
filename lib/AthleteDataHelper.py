import requests
import logging

logger = logging.getLogger(__name__)


def get_athlete_activities(access_token):
    activity_data = None
    url = f"https://www.strava.com/api/v3/athlete/activities"
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + access_token}

    r = requests.get(url, headers=headers)

    request_status = r.status_code
    if request_status == 200:
        activity_data = r.json()
    else:
        logger.error(request_status)

    return activity_data
