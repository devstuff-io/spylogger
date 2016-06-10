import logging
import logging.config
import os

LOG_LOGGER = os.getenv('SPY_LOG_LOGGER', 'json-flat')
LOG_LEVEL = os.getenv('SPY_LOG_LEVEL', 'ERROR')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {'()': 'spylogger.formatters.JSONLogFormatter'},
        'json-flat': {'()': 'spylogger.formatters.JSONFlatLogFormatter'},
        "ugly": {"format": "%(asctime)s %(levelname)s: %(module)s.%(funcName)s:%(lineno)d  [%(message)s]"}
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'json',
            'stream': 'ext://sys.stdout'
        },
        'cw': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'json-flat',
            'stream': 'ext://sys.stdout'
        },
        'ugly': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'ugly',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        'json-flat': {'level': LOG_LEVEL, 'handlers': ['cw']},
        'json': {'level': LOG_LEVEL, 'handlers': ['console']},
        'ugly': {'level': LOG_LEVEL, 'handlers': ['ugly']},
    }
}


def get_logger(name=LOG_LOGGER, log_level=LOG_LEVEL):
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    return logger
