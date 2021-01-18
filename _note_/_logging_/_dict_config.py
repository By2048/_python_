import logging
import logging.config

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "local": {
            "format": '[%(levelname)1.1s %(asctime)s %(module)12s:%(lineno)4d] %(message)s',
            'datefmt': '%H:%M:%S'
        },
    },
    "handlers": {
        "local": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "local",
            "stream": "ext://sys.stdout"
        },
    },
    "loggers": {
        "local": {
            "handlers": ["local"],
            "propagate": False
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["local"],
        "propagate": False
    }
}

logging.config.dictConfig(LOG_CONFIG)
