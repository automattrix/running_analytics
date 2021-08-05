import unittest
from lib.utils.environment.env import load_params


class TestLoadParams(unittest.TestCase):

    def test_load_token_params(self):
        result = load_params(p_key='TOKEN')
        self.assertIsInstance(result, dict)

    def test_load_database_params(self):
        result = load_params(p_key='DATABASE')
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()

