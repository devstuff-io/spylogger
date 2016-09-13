import sys
from collections import Mapping
from copy import deepcopy
from datetime import datetime
from logging import Formatter

try:
    import simplejson as json
except ImportError:
    import json

from spylogger import settings


class BaseLogFormatter(Formatter):

    def get_src_location_string(self, record):
        return '%s.%s:%d' % (record.__dict__.get('module'), record.__dict__.get('funcName'), record.__dict__.get('lineno'))

    def get_meta(self, record):
        meta = {}
        for key in record.__dict__.keys():
            if key in settings.JSON_LOG_KEYS:
                meta[key] = record.__dict__.get(key)
        return meta

    def get_msg(self, record):
        try:
            return deepcopy(record.__dict__.get('msg'))
        except:
            return record.__dict__.get('msg')

    def build_msg(self, record, show_meta=settings.SHOW_META):
        logmsg = self.get_msg(record)
        if show_meta:
            if not isinstance(logmsg, Mapping):
                logmsg = {'message': logmsg}
            logmsg['__meta'] = self.get_meta(record)
        return logmsg

    @classmethod
    def format_timestamp(cls, time):
        tstamp = datetime.utcfromtimestamp(time)
        return tstamp.strftime("%Y-%m-%dT%H:%M:%S") + ".%03d" % (tstamp.microsecond / 1000) + "Z"

    @classmethod
    def serialize(cls, message):
        if sys.version_info < (3, 0):
            return json.dumps(message)
        return bytes(json.dumps(message), 'utf-8')


class JSONBaseLogFormatter(BaseLogFormatter):

    divider = '\033[1;30m{}\033[0m'.format('.' * 53)

    def get_message_divider(self, record, msg=''):
        div = '==={0:{fill}<50}'.format(msg, fill='=')
        return '\033[1;30m{}\033[0m'.format(div)

    def format_msg(self, logmsg):
        try:
            return self.dumps(logmsg)
        except TypeError:
            return logmsg

    def dumps(self, logmsg, json_dumps_opts=dict()):
        return json.dumps(logmsg, **json_dumps_opts)


class JSONLogFormatter(JSONBaseLogFormatter):

    def format(self, record):
        record.msg = "{div}\n{msg}\n{hr}".format(
            div=self.get_message_divider(record, self.get_src_location_string(record)),
            msg=self.format_msg(self.build_msg(record)),
            hr=self.divider
        )
        return super(JSONLogFormatter, self).format(record)


class JSONPrettifiedLogFormatter(JSONLogFormatter):

    def dumps(self, logmsg):
        return json.dumps(logmsg, indent=4)


class SrcLocationAsKeyLogFormatter(JSONPrettifiedLogFormatter):

    def get_msg(self, record):
        src_loc = self.get_src_location_string(record)
        return {src_loc: deepcopy(record.__dict__.get('msg'))}

    def format(self, record):
        record.msg = "{msg}\n{hr}".format(
            msg=self.format_msg(self.build_msg(record, False)),
            hr=self.divider
        )
        return BaseLogFormatter.format(self, record)
