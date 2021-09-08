import requests
import logging
import hashlib
import json
from lib.utils.common import epoch_days_in_past

logger = logging.getLogger(__name__)


def get_athlete_activities(access_token, page=None, before=None, after=None, per_page=None):
    """
    Return json dict of athlete "activity overview" data
    :param access_token:
    :param page: Number of pages
    :param before: Return activities before this date
    :param after: Return activities after this date
    :param per_page: Number of activities per page, default 30
    :return:
    """

    body = {}

    if page is not None:
        body['page'] = page

    if after is not None:
        # convert after into epoch time
        epoch_timestamp = epoch_days_in_past(num_days=after)
        body['after'] = epoch_timestamp

    if before is not None:
        epoch_timestamp = epoch_days_in_past(num_days=before)
        body['before'] = epoch_timestamp

    if per_page is not None:
        body['per_page'] = per_page

    activity_data = None
    url = f"https://www.strava.com/api/v3/athlete/activities"
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + access_token}

    r = requests.get(url, data=json.dumps(body), headers=headers)

    request_status = r.status_code
    if request_status == 200:
        activity_data = r.json()
    else:
        logger.error(request_status)

    return activity_data


def remove_map_polyline_from_dataset(df):
    clean_df = df.copy()
    try:
        clean_df = df.drop(['map'], axis=1)
    except Exception as e:
        logger.debug(e)
        logger.error("Unable to remove map column from dataset")
    return clean_df


def create_activity_id_hash(athlete, activityid, start_date):
    athlete = athlete['id']
    string_input = f"{athlete}-{activityid}-{start_date}"
    result = hashlib.md5(string_input.encode())
    result_hex = str(result.hexdigest())
    return result_hex


def convert_meters_to_miles(distance):
    miles = None
    m_to_mi = 1609.34
    try:
        miles = float(distance) / m_to_mi
    except Exception as e:
        logger.debug(e)
        logger.error("Unable to convert distance to miles")
    return miles


def apply_send_data_to_es(es, es_index, data):
    id_hash = data['id_hash'].iloc[0]
    data = data.drop(['id_hash'], axis=1)
    es_data_dict = data.to_dict()
    es_data = json.dumps(es_data_dict)
    print("Test)")
    print(es_data)
    es.index(index=es_index, id=id_hash, body=es_data)
    #exit()
