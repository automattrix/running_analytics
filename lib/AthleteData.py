from lib.metrics.elasticsearch_data import ElasticHelper
from lib.utils.auth.token_handling import request_token
from lib.utils.environment.env import load_params
from lib.AthleteDataHelper import get_athlete_activities, remove_map_polyline_from_dataset, create_activity_id_hash, \
    apply_send_data_to_es, convert_meters_to_miles
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(10)


class Athlete:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.database_params = load_params(p_key='DATABASE')
        self.token_params = load_params(p_key='TOKEN')
        self.es_params = load_params(p_key='ELASTICSEARCH')
        self.strava_params = load_params(p_key='STRAVA_RESULTS')
        self.access_token_dict = None

        self.activities_raw = None
        self.activities_processed = []

    def authorize(self):
        self.access_token_dict = request_token(token_params=self.token_params)
        logger.info(self.access_token_dict)

    def query_athlete_activities(self):
        activities_params = self.strava_params['ACTIVITIES_OVERVIEW']
        self.activities_raw = get_athlete_activities(
            access_token=self.access_token_dict['access_token'],
            after=activities_params['AFTER'],
            per_page=activities_params['PER_PAGE']
        )
        logger.debug(self.activities_raw)
        logger.info(f"Number of activities:\t[{len(self.activities_raw)}]")

    def preprocess_athlete_data(self):
        logger.info("Preprocessing data")

        raw_data_list = self.activities_raw
        for raw_dict in raw_data_list:
            df_raw = pd.DataFrame([raw_dict])
            # Remove "map polyline"
            df_processed = remove_map_polyline_from_dataset(df=df_raw)
            # Generate athlete activityid hash
            df_processed['id_hash'] = df_processed.apply(
                lambda x: create_activity_id_hash(
                    athlete=x['athlete'],
                    activityid=x['id'],
                    start_date=x['start_date']
                ), axis=1
            )
            # Convert meters to miles
            df_processed['distance_miles'] = df_processed['distance'].apply(convert_meters_to_miles)
            self.activities_processed.append(df_processed)

    def send_data_to_es(self):
        logger.info("Sending data to ElasticSearch")
        es_helper = ElasticHelper(params=self.es_params)
        es_connection = es_helper.connect_es()
        for df in self.activities_processed:
            apply_send_data_to_es(es=es_connection, es_index='test-es-running', data=df)

