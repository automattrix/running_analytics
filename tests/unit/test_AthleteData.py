import unittest
from lib.AthleteData import Athlete


class TestAthlete(unittest.TestCase):

    def test_authorize(self):
        athlete = Athlete(name="Matt Karan")
        athlete.authorize()
        result = athlete.access_token_dict
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
