from lib.utils.auth.token_handling import request_token
from lib.utils.environment.env import load_params

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

    def authorize(self):
        self.access_token_dict = request_token(token_params=self.token_params)
        logger.info(self.access_token_dict)
