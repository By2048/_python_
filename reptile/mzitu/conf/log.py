import logging.config

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "local": {
            "format": '[%(levelname)1.1s %(asctime)s %(module)15s:%(lineno)3d] %(message)s',
            'datefmt': '%H:%M:%S'
        },
    },
    "handlers": {
        "local": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "local",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "local": {
            "handlers": ["local"],
            "propagate": False
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["local"],
        "propagate": False
    }
}

if __name__ == '__main__':
    logging.config.dictConfig(LOG_CONFIG)
    logging.info('Hello, log')
