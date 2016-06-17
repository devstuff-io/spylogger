spylogger
=========

Generic python logging library.


Installation
============

.. code-block:: python

   pip install spylogger

Usage
=====

.. code-block:: python

   from spylogger import get_logger
   logger = get_logger()
   logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True})


**Environment Variables:**

``SPY_LOG_LOGGER``

The configured logger name. Available loggers:

* json-flat (Default)
* json
* json-src-key
* ugly

``SPY_LOG_LEVEL``

The python log level. See the docs_

.. code-block:: python

   get_logger(name=SPY_LOG_LOGGER, log_level=SPY_LOG_LEVEL)

``SPY_JSON_LOG_KEYS``

A list of log record keys to put in the ``__meta`` section of the log message.
**Default**: ``threadName``, ``process``, ``args``, ``module``, ``levelname``, ``pathname``, ``lineno``, ``funcName``

``SPY_SHOW_META``

Flag for showing the ``__meta`` output. **Default**: True

Authors
=======

See contributors section on GitHub.

.. _docs: https://docs.python.org/2/howto/logging.html#logging-levels
