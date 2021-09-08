import datetime
import logging

logger = logging.getLogger(__name__)


def epoch_days_in_past(num_days):
    """
    Return epoch timestamp of 'now' minus 'num_days'
    :param num_days:
    :return:
    """
    epoch_past = None
    try:
        date_past = datetime.datetime.now() - datetime.timedelta(days=num_days)
        epoch_past = date_past.timestamp()
    except Exception as e:
        logger.debug(e)
        logger.error("Unable to convert to epoch timestamp")

    return epoch_past
