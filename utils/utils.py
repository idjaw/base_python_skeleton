import site
import sys
import os
from settings import settings

# Set up the virtualenv proper site-packages path and start the virtualenv
def configure_virtualenv():
	# Configure the virtualenv folder structure
	prev_sys_path = list(sys.path)
	# add the site-packages of our virtualenv as a site dir
	site.addsitedir(os.path.join(
		settings.PROJECT_ROOT, settings.VIRTUALENV_PATH
	))
	# Add the app's directory to the PYTHONPATH
	sys.path.append(os.path.dirname(__file__))
	# reorder sys.path so new directories from the addsitedir show up first
	new_sys_path = [p for p in sys.path if p not in prev_sys_path]
	for item in new_sys_path:
	    sys.path.remove(item)
	sys.path[:0] = new_sys_path
	# Activate your virtual env
	activate_path = os.path.join(
		settings.PROJECT_ROOT, settings.VIRTUALENV_ACTIVATE_PATH
	)
	activate_env=os.path.expanduser(activate_path)
	execfile(activate_env, dict(__file__=activate_env))

	# Raise an exception if virtualenv is not started
	if not hasattr(sys, 'real_prefix'):
		raise Exception("virtualenv could not be started...Exiting")