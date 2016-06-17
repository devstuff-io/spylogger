from spylogger import get_logger
from datetime import datetime

logger = get_logger()

# log_level = 'INFO'
# logger = get_logger('json', log_level)
# logger = get_logger('json-flat', log_level)
# logger = get_logger('json-src-key', log_level)
# logger = get_logger('ugly', log_level)

logger.error('test Pretty error message.')
logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
logger.warning({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
logger.debug({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True, 'datetime': datetime.now()})

try:
    foo['none']
except Exception as e:
    logger.exception(e)
