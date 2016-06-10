# spylogger

Python logging handler for SPS libraries.

* [Installation](#installation)
* [Usage](#usage)
* [Authors](#authors)


---

<a name="installation" id="installation"></a>

## Installation

```bash
pip install -e git+git@github.com:SPSCommerce/spylogger.git#egg=spylogger
```

---

<a name="usage" id="usage"></a>

## Usage

```python
from spylogger import get_logger
logger = get_logger()
logger.info({'string': 'test Pretty info message.', 'int': 42, 'bool': True})
```

### Documentation

#### Environment Variables:

##### `SPY_LOG_LOGGER`

The configured logger name. Available loggers:

* json-flat (Default)
* json
* ugly


##### `SPY_LOG_LEVEL`

The python log level. See the [docs](https://docs.python.org/2/howto/logging.html#logging-levels)


```python
get_logger(name=SPY_LOG_LOGGER, log_level=SPY_LOG_LEVEL)
```

---

<a name="authors" id="authors"></a>

## Authors

See contributors section on GitHub.
