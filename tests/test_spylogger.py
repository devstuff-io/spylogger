import os
from unittest import TestCase

from testfixtures import log_capture

import spylogger


class SpyloggerTest(TestCase):

    @log_capture()
    def test_basic_log(self, capture):
        os.environ['SPY_SHOW_META'] = '0'
        logger = spylogger.get_logger()
        logger.error('bar')
        print('-' * 80)
        print('dir capture ---------------')
        for d in dir(capture):
            print(d)
        print('-' * 80)
        print('capture.actual ---------------')
        print(capture.actual())
        print('-' * 80)
        print('capture.__dict__.keys ---------------')
        for d in capture.__dict__.keys():
            print(d)
        print('-' * 80)
        print('capture.old ---------------')
        print(capture.old)
        print('-' * 80)
        # capture.check(
        #     ('json-flat', 'ERROR', '\x1b[1;30m===test_spylogger.test_basic_log:14==================\x1b[0m\n{"message": "bar", "__meta": {"args": [], "process": 97240, "threadName": "MainThread", "module": "test_spylogger", "funcName": "test_basic_log", "pathname": "/Users/megan/dev/spylogger/tests/test_spylogger.py", "lineno": 14, "levelname": "ERROR"}}\n\x1b[1;30m.....................................................\x1b[0m'),
        # )
