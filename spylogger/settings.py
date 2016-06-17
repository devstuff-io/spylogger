import os

JSON_DEFAULT_LOG_KEYS = ['threadName', 'process', 'args', 'module', 'levelname', 'pathname', 'lineno', 'funcName']
JSON_LOG_KEYS = os.getenv('SPY_JSON_LOG_KEYS', JSON_DEFAULT_LOG_KEYS)
if not isinstance(JSON_LOG_KEYS, list):
    try:
        JSON_LOG_KEYS = JSON_LOG_KEYS.split(',')
    except:
        JSON_LOG_KEYS = JSON_DEFAULT_LOG_KEYS

LOG_LOGGER = os.getenv('SPY_LOG_LOGGER', 'json-flat')
LOG_LEVEL = os.getenv('SPY_LOG_LEVEL', 'ERROR')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {'()': 'spylogger.formatters.JSONPrettifiedLogFormatter'},
        'json-flat': {'()': 'spylogger.formatters.JSONLogFormatter'},
        'json-src-key': {'()': 'spylogger.formatters.SrcLocationAsKeyLogFormatter'},
        "ugly": {"format": "%(asctime)s %(levelname)s: %(module)s.%(funcName)s:%(lineno)d  [%(message)s]"}
    },
    'handlers': {
        'json': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'json',
            'stream': 'ext://sys.stdout'
        },
        'json-src-key': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'json-src-key',
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
        'json': {'level': LOG_LEVEL, 'handlers': ['json']},
        'json-src-key': {'level': LOG_LEVEL, 'handlers': ['json-src-key']},
        'ugly': {'level': LOG_LEVEL, 'handlers': ['ugly']},
    }
}

SHOW_META = os.getenv('SPY_SHOW_META', True)
if isinstance(SHOW_META, str):
    SHOW_META = 'true' in [SHOW_META.lower()]
