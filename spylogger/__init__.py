import logging
import logging.config

from spylogger.settings import LOG_LOGGER, LOG_LEVEL, LOGGING

try:
    import spylogger.pretty
    LOGGING['formatters']['pretty'] = {'()': 'spylogger.pretty.PrettyJSONLogFormatter'}
    LOGGING['handlers']['pretty'] = {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'pretty',
        'stream': 'ext://sys.stdout'
    }
    LOGGING['loggers']['pretty'] = {'level': LOG_LEVEL, 'handlers': ['pretty']}

    LOGGING['formatters']['pretty-no-meta'] = {'()': 'spylogger.pretty.NoMetaPrettyJSONLogFormatter'}
    LOGGING['handlers']['pretty-no-meta'] = {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'pretty-no-meta',
        'stream': 'ext://sys.stdout'
    }
    LOGGING['loggers']['pretty-no-meta'] = {'level': LOG_LEVEL, 'handlers': ['pretty-no-meta']}
except ImportError:
    pass


def get_logger(name=LOG_LOGGER, log_level=LOG_LEVEL):
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    return logger
