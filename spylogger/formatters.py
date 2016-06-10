import os
import sys
from collections import Mapping
from copy import deepcopy
from datetime import datetime
from logging import Formatter

try:
    import simplejson as json
except ImportError:
    import json


JSON_DEFAULT_LOG_KEYS = ['threadName', 'process', 'args', 'module', 'levelname', 'pathname', 'lineno', 'funcName']
JSON_LOG_KEYS = os.getenv('SPS_JSON_LOG_KEYS', JSON_DEFAULT_LOG_KEYS)
if not isinstance(JSON_LOG_KEYS, list):
    try:
        JSON_LOG_KEYS = JSON_LOG_KEYS.split(',')
    except:
        JSON_LOG_KEYS = JSON_DEFAULT_LOG_KEYS


class BaseLogFormatter(Formatter):

    @classmethod
    def format_timestamp(cls, time):
        tstamp = datetime.utcfromtimestamp(time)
        return tstamp.strftime("%Y-%m-%dT%H:%M:%S") + ".%03d" % (tstamp.microsecond / 1000) + "Z"

    @classmethod
    def serialize(cls, message):
        if sys.version_info < (3, 0):
            return json.dumps(message)
        return bytes(json.dumps(message), 'utf-8')


class JSONLogFormatter(BaseLogFormatter):

    def format(self, record):
        logmsg = deepcopy(record.__dict__.get('msg'))
        if not isinstance(logmsg, Mapping):
            logmsg = {'message': logmsg}

        meta = {}
        for key in record.__dict__.keys():
            if key in JSON_LOG_KEYS:
                meta[key] = record.__dict__.get(key)
        logmsg['__meta'] = meta

        title = '%s.%s:%d' % (record.__dict__.get('module'), record.__dict__.get('funcName'), record.__dict__.get('lineno'))
        div = '==={0:{fill}<50}'.format(title, fill='=')

        try:
            msg = self.dumps(logmsg)
        except TypeError:
            msg = logmsg

        record.msg = "{div}\n{msg}\n{hr}".format(
            div='\033[1;30m{}\033[0m'.format(div),
            msg=msg,
            hr='\033[1;30m{}\033[0m'.format('.' * 53)
        )
        return super(JSONLogFormatter, self).format(record)

    def dumps(self, logmsg):
        return json.dumps(logmsg, indent=4)


class JSONFlatLogFormatter(JSONLogFormatter):

    def dumps(self, logmsg):
        return json.dumps(logmsg)
