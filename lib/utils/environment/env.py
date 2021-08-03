import yaml
from pathlib import Path
import sys
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(10)


def set_env(project_path):
    project_path = Path(project_path).expanduser().resolve()
    src_path = str(project_path)
    logger.debug(project_path)
    logger.debug(src_path)

    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    if "PYTHONPATH" not in os.environ:
        os.environ["PYTHONPATH"] = src_path

    if os.getcwd() != str(project_path):
        logger.info(f"Changing the current working directory to {str(project_path)}")
        os.chdir(str(project_path))


def load_params(p_key):
    """
    Create parameters dictionary from yaml.
    Read ./conf/base/ params, override if values defined in ./conf/local/
    :param p_key:
    :return:
    """

    params_dict = {}
    try:
        with open('./conf/base/params.yaml') as p_base:
            params = yaml.load(p_base, Loader=yaml.FullLoader)
            for k, v in params['PARAMS'][p_key].items():
                params_dict[k] = v
        p_base.close()
    except FileNotFoundError as e:
        logger.debug('Base parameters missing')
        raise e

    try:
        with open('./conf/local/params.yaml') as p_local:
            params = yaml.load(p_local, Loader=yaml.FullLoader)
            for k, v in params['PARAMS'][p_key].items():
                params_dict[k] = v
        p_local.close()
    except Exception as e:
        logger.info('No local override parameters specified. Using base parameters')
        logger.debug(e)

    return params_dict
