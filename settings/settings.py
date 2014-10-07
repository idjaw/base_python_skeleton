import sys
import os


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# virtualenv settings
PYTHON_VER = "Python%s.%s" % (sys.version_info.major, sys.version_info.minor)
VIRTUALENV_NAME = 'venv'
VIRTUALENV_PATH = '%s/lib/%s/site-packages/' % (VIRTUALENV_NAME, PYTHON_VER)
VIRTUALENV_ACTIVATE_PATH = '%s/bin/activate_this.py' % VIRTUALENV_NAME

# logging settings
LOG_FILEPATH = '%s/%s' % (PROJECT_ROOT, 'debug.log')
LOG_LEVEL = 'DEBUG'

