import logging
import logging.config

from spylogger.settings import LOG_LOGGER, LOG_LEVEL, LOGGING


def get_logger(name=LOG_LOGGER, log_level=LOG_LEVEL):
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    return logger
