import os
import unittest
from lib.utils.environment.env import set_env
from tests.unit import test_env, test_AthleteData
import logging

logger = logging.getLogger(__name__)
logger.setLevel(10)

# unit tests
unit_loader = unittest.TestLoader()
unit_suite = unittest.TestSuite()

unit_suite.addTests(unit_loader.loadTestsFromModule(test_env))
unit_suite.addTests(unit_loader.loadTestsFromModule(test_AthleteData))
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(unit_suite)
logger.info(result)


# integration tests
# integration_loader = unittest.TestLoader()
# integration_suite = unittest.TestSuite()
#
# integration_suite.addTests(integration_loader.loadTestsFromModule())


if __name__ == '__main__':
    logger.debug(os.path.dirname(os.path.realpath(__file__)))
    set_env(project_path=os.path.dirname(os.path.realpath(__file__)))
