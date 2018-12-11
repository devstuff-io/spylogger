[![Build Status](https://travis-ci.org/devstuff-io/spylogger.svg?branch=master)](https://travis-ci.org/devstuff-io/spylogger)

# spylogger

Generic python logging library.

## Documentation:

- https://github.com/devstuff-io/spylogger
- https://docs.python.org/2/howto/logging.html#logging-levels


## Installation

### basic loggers

This installs spylogger only and will load the loggers with no external dependency requirements.

```bash
pip install spylogger
```


### pretty loggers

This installs spylogger, pygments, and pygments-json and loads the basic loggers along with pretty loggers.

```bash
pip install spylogger[pretty]
```


## Configuration

### Environment Variables

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SPY_LOG_LOGGER</td>
      <td>
        <p>The configured logger name.</p>
        Available loggers:
        <ul>
          <li>json-flat</li>
          <li>json</li>
          <li>json-clean</li>
          <li>json-src-key</li>
          <li>pretty</li>
          <li>pretty-no-meta</li>
          <li>ugly</li>
        </ul>
      </td>
      <td>json-flat</td>
  </tr>
  <tr>
    <td>SPY_LOG_LEVEL</td>
    <td>The python log level. See the python documentation</td>
    <td>WARNING</td>
  </tr>
  <tr>
    <td>SPY_SHOW_META</td>
    <td>Flag for showing the `__meta` output.</td>
    <td>True</td>
  </tr>
  <tr>
    <td>SPY_JSON_LOG_KEYS</td>
    <td>
      <p>A list of log record keys to put in the `__meta` section of the log message.</p>
      Available Keys:
      <ul>
        <li>args</li>
        <li>created</li>
        <li>exc_info</li>
        <li>exc_text</li>
        <li>filename</li>
        <li>funcName</li>
        <li>levelname</li>
        <li>levelno</li>
        <li>lineno</li>
        <li>module</li>
        <li>msecs</li>
        <li>msg</li>
        <li>name</li>
        <li>pathname</li>
        <li>process</li>
        <li>processName</li>
        <li>relativeCreated</li>
        <li>thread</li>
        <li>threadName</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>args</li>
        <li>funcName</li>
        <li>levelname</li>
        <li>lineno</li>
        <li>module</li>
        <li>pathname</li>
        <li>process</li>
        <li>threadName</li>
      </ul>
    </td>
  </tr>
  </tbody>
</table>


### Pretty Formatter Styles

See the [pygments documentation](http://pygments.org/docs/styles/)


**Environment Variables**

Name                           | Default
-------------------------------|-----------
`SPY_LOG_FORMATTER_DEBUG`      | autumn
`SPY_LOG_FORMATTER_INFO`       | monokai
`SPY_LOG_FORMATTER_WARNING`    | fruity
`SPY_LOG_FORMATTER_ERROR`      | default
`SPY_LOG_FORMATTER_CRITICAL`   | vs


**Available styles**

```bash
python -c "from pygments.styles import get_all_styles;print list(get_all_styles())"
```


## Usage

```python
from spylogger import get_logger

# get_logger(name=SPY_LOG_LOGGER, log_level=SPY_LOG_LEVEL)
logger = get_logger()

logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
```

More examples are in example.py


## Authors

See contributors section on GitHub.
