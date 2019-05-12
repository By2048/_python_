import logging

try:
    from mzitu.conf.log import LOG_CONFIG
except ImportError:
    from conf.log import LOG_CONFIG

logging.config.dictConfig(LOG_CONFIG)
