from lib.AthleteData import Athlete
from lib.utils.environment.env import set_env
import os
import logging


logger = logging.getLogger(__name__)
logger.setLevel(10)


def main():
    athlete_insights = Athlete(name='Matt Karan')
    athlete_insights.authorize()
    athlete_insights.query_athlete_activities()


if __name__ == '__main__':
    logger.debug(os.path.dirname(os.path.realpath(__file__)))
    set_env(project_path=os.path.dirname(os.path.realpath(__file__)))
    main()
