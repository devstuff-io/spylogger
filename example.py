from spylogger import get_logger
from datetime import datetime

logger = get_logger()
# logger = get_logger('json')
# logger = get_logger('json-flat')
# logger = get_logger('ugly')

logger.error('test Pretty error message.')
logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
logger.warning({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
logger.debug({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True, 'datetime': datetime.now()})

try:
    foo['none']
except Exception as e:
    logger.exception(e)
