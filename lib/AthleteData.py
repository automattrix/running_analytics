from lib.utils.auth.token_handling import request_token
from lib.utils.environment.env import load_params


class Athlete:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.database_params = load_params(p_key='DATABASE')
        self.token_params = load_params(p_key='TOKEN')

    def authorize(self):
        request_token(token_params=self.token_params)
