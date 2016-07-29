from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygson.json_lexer import JSONLexer

from spylogger import settings
from spylogger.formatters import JSONPrettifiedLogFormatter


class PrettyJSONLogFormatter(JSONPrettifiedLogFormatter):

    style = settings.LOG_FORMATTER_DEBUG

    def get_log_style(self, level):
        if level >= 41:
            return settings.LOG_FORMATTER_CRITICAL
        elif level >= 31:
            return settings.LOG_FORMATTER_ERROR
        elif level >= 21:
            return settings.LOG_FORMATTER_WARNING
        elif level >= 11:
            return settings.LOG_FORMATTER_INFO
        return settings.LOG_FORMATTER_DEBUG

    def format(self, record):
        self.style = self.get_log_style(record.levelno)
        return super(PrettyJSONLogFormatter, self).format(record)

    def format_msg(self, logmsg):
        try:
            return highlight(
                self.dumps(logmsg),
                JSONLexer(),
                Terminal256Formatter(style=self.style)
            ).strip()
        except TypeError:
            return logmsg
