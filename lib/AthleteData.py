from lib.utils.auth.token_handling import request_token
from lib.utils.environment.env import load_params
from lib.AthleteDataHelper import get_athlete_activities
import logging

logger = logging.getLogger(__name__)
logger.setLevel(10)


class Athlete:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.database_params = load_params(p_key='DATABASE')
        self.token_params = load_params(p_key='TOKEN')

        self.access_token_dict = None

        self.activities_raw = None

    def authorize(self):
        self.access_token_dict = request_token(token_params=self.token_params)
        logger.info(self.access_token_dict)

    def query_athlete_activities(self):
        self.activities_raw = get_athlete_activities(
            access_token=self.access_token_dict['access_token']
        )
        logger.info(self.activities_raw)
