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
* ugly

``SPY_LOG_LEVEL``

The python log level. See the docs_

.. code-block:: python

   get_logger(name=SPY_LOG_LOGGER, log_level=SPY_LOG_LEVEL)


Authors
=======

See contributors section on GitHub.

.. _docs: https://docs.python.org/2/howto/logging.html#logging-levels
