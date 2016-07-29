from spylogger import get_logger
from datetime import datetime

log_level = 'DEBUG'
logger = get_logger('pretty', log_level)
# logger = get_logger('json', log_level)
# logger = get_logger('json-flat', log_level)
# logger = get_logger('json-src-key', log_level)
# logger = get_logger('ugly', log_level)
# logger = get_logger()

logger.error('test error log message.')
logger.info({'string': 'test info log message.', 'int': 42, 'bool': True})
logger.warning({'string': 'test warning log message.', 'int': 42, 'bool': True})
logger.debug({'string': 'test debug log message.', 'int': 42, 'bool': True})
logger.info({'string': 'test info log message with datetime.', 'int': 42, 'bool': True, 'datetime': datetime.now()})

try:
    foo['none']
except Exception as e:
    logger.exception(e)
