import os
import logging
import logging.handlers

def init(filepath=None, name="log", level="INFO"):
    filepath = filepath or 'debug.log'
    format = ("%(asctime)s %(levelname)s [%(threadName)s] - %(message)s - (%(module)s - %(funcName)s)")

    # create the log directory if it doesn't exist
    if filepath and not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    logging.basicConfig(level=getattr(logging, level),
                        format=format,
                        datefmt='%Y-%m-%d %H:%M:%S')

    while len(logging.getLogger().handlers) is not 0:
        logging.getLogger().handlers.pop()

    # create the rotating file handler
    handler = logging.FileHandler(filepath)
    handler.setLevel(getattr(logging, level))
    handler.setFormatter(logging.Formatter(format))

    logging.getLogger().addHandler(handler)