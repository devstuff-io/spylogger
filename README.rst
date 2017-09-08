spylogger
=========

Generic python logging library.

Documentation: https://github.com/devstuff-io/spylogger


Installation
------------

basic loggers
.............

This installs spylogger only and will load the loggers with no external dependency requirements.

.. code-block:: python

   pip install spylogger


pretty loggers
..............

This installs spylogger, pygments, and pygments-json and loads the basic loggers along with pretty loggers.

.. code-block:: python

   pip install spylogger[pretty]


Configuration
-------------

Environment Variables
.....................

+------------------------+-------------------------------------------------+-------------------+
| Name                   | Description                                     | Default           |
+========================+=================================================+===================+
| ``SPY_LOG_LOGGER``     | The configured logger name.                     | json-flat         |
|                        | Available loggers:                              |                   |
|                        |                                                 |                   |
|                        | * json-flat (Default)                           |                   |
|                        | * json                                          |                   |
|                        | * json-src-key                                  |                   |
|                        | * pretty                                        |                   |
|                        | * pretty-no-meta                                |                   |
|                        | * ugly                                          |                   |
+------------------------+-------------------------------------------------+-------------------+
| ``SPY_LOG_LEVEL``      | The python log level.                           | WARNING           |
|                        | See the docs_                                   |                   |
+------------------------+-------------------------------------------------+-------------------+
| ``SPY_SHOW_META``      | Flag for showing the ``__meta`` output.         | True              |
+------------------------+-------------------------------------------------+-------------------+
| ``SPY_JSON_LOG_KEYS``  | A list of log record keys to put in the         |                   |
|                        | ``__meta`` section of the log message.          |                   |
|                        |                                                 | - ``args``        |
|                        |                                                 | - ``funcName``    |
|                        | **Available Keys**:                             | - ``levelname``   |
|                        |                                                 | - ``lineno``      |
|                        | * ``args``                                      | - ``module``      |
|                        | * ``created``                                   | - ``pathname``    |
|                        | * ``exc_info``                                  | - ``process``     |
|                        | * ``exc_text``                                  | - ``threadName``  |
|                        | * ``filename``                                  |                   |
|                        | * ``funcName``                                  |                   |
|                        | * ``levelname``                                 |                   |
|                        | * ``levelno``                                   |                   |
|                        | * ``lineno``                                    |                   |
|                        | * ``module``                                    |                   |
|                        | * ``msecs``                                     |                   |
|                        | * ``msg``                                       |                   |
|                        | * ``name``                                      |                   |
|                        | * ``pathname``                                  |                   |
|                        | * ``process``                                   |                   |
|                        | * ``processName``                               |                   |
|                        | * ``relativeCreated``                           |                   |
|                        | * ``thread``                                    |                   |
|                        | * ``threadName``                                |                   |
|                        |                                                 |                   |
|                        | See the python docs_                            |                   |
+------------------------+-------------------------------------------------+-------------------+

Pretty Formatter Styles
.......................

See the pygments documentation_


**Environment Variables**

+--------------------------------+----------+
| Name                           | Default  |
+================================+==========+
| ``SPY_LOG_FORMATTER_DEBUG``    | autumn   |
+--------------------------------+----------+
| ``SPY_LOG_FORMATTER_INFO``     | monokai  |
+--------------------------------+----------+
| ``SPY_LOG_FORMATTER_WARNING``  | fruity   |
+--------------------------------+----------+
| ``SPY_LOG_FORMATTER_ERROR``    | default  |
+--------------------------------+----------+
| ``SPY_LOG_FORMATTER_CRITICAL`` | vs       |
+--------------------------------+----------+


**Available styles**

.. code-block:: shell

   python -c "from pygments.styles import get_all_styles;print list(get_all_styles())"


Usage
-----

.. code-block:: python

   from spylogger import get_logger

   # get_logger(name=SPY_LOG_LOGGER, log_level=SPY_LOG_LEVEL)
   logger = get_logger()

   logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True})


More examples are in example.py


Authors
-------

See contributors section on GitHub.


.. _docs: https://docs.python.org/2/howto/logging.html#logging-levels
.. _documentation: http://pygments.org/docs/styles/
