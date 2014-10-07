from settings import settings
from utils import utils
from utils import logger
import logging
import requests

logger.init(filepath=settings.LOG_FILEPATH, level=settings.LOG_LEVEL)
log = logging.getLogger('main')
# configure the virtualenv environment
utils.configure_virtualenv()

r = requests.get('http://www.google.ca')

if __name__ == '__main__':
	pass