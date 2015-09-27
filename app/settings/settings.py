from os.path import abspath, join, dirname

PROJECT_ROOT = abspath(join(dirname(__file__), '..'))

# logging settings
DEBUG_LOG_NAME = 'debug.log'
LOG_FILE_PATH = '{PROJECT_ROOT}/{DEBUG_LOG_NAME}'.format(**globals())
FILE_LOG_LEVEL = 'DEBUG'
