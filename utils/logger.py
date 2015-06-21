import os
import logging
import logging.handlers
from settings.settings import FILE_LOG_LEVEL, LOG_FILE_PATH


def init():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s - (%(module)s - %(funcName)s) - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    filepath = LOG_FILE_PATH or 'debug.log'
    if filepath and not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    file_handler = logging.FileHandler(filepath)
    file_handler.setLevel(getattr(logging, FILE_LOG_LEVEL))
    file_handler.setFormatter(formatter)

    logging.getLogger().addHandler(file_handler)

