import os

ENV_PREFIX = 'SPY_'


def get_env(name, default):
    return os.getenv('{prefix}{variable}'.format(prefix=ENV_PREFIX, variable=name), default)


JSON_DEFAULT_LOG_KEYS = ['threadName', 'process', 'args', 'module', 'levelname', 'pathname', 'lineno', 'funcName']
JSON_LOG_KEYS = get_env('JSON_LOG_KEYS', JSON_DEFAULT_LOG_KEYS)
if not isinstance(JSON_LOG_KEYS, list):
    try:
        JSON_LOG_KEYS = JSON_LOG_KEYS.split(',')
    except:
        JSON_LOG_KEYS = JSON_DEFAULT_LOG_KEYS


SHOW_META = get_env('SHOW_META', True)
if isinstance(SHOW_META, str):
    SHOW_META = 'true' in [SHOW_META.lower()]


LOG_FORMATTER_DEBUG = get_env('LOG_FORMATTER_DEBUG', 'autumn')
LOG_FORMATTER_INFO = get_env('LOG_FORMATTER_INFO', 'monokai')
LOG_FORMATTER_WARNING = get_env('LOG_FORMATTER_WARNING', 'fruity')
LOG_FORMATTER_ERROR = get_env('LOG_FORMATTER_ERROR', 'default')
LOG_FORMATTER_CRITICAL = get_env('LOG_FORMATTER_CRITICAL', 'vs')


LOG_LOGGER = get_env('LOG_LOGGER', 'json-flat')
LOG_LEVEL = get_env('LOG_LEVEL', 'WARNING')


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
