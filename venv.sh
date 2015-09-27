#!/bin/sh

#####
#    This shell wrapper will call an external application with its
#    appropriate parameters and run from its own venv
#####

APPLICATION_PATH='app'

PYTHON_VENV_LOCATION=${APPLICATION_PATH}'/venv/'

PYTHON_EXECUTABLE_LOCATION=${PYTHON_VENV_LOCATION}'/bin/python'

# Main Application
APPLICATION_NAME='run.py'

create_venv() {
    echo `cd ${APPLICATION_PATH} ; virtualenv venv ; source venv/bin/activate ; pip install -r setup-requires`
}

help_info () {
    echo "$package - Add some useful information here"
    echo " "
    echo "$package [options]"
    echo " "
    echo "options:"
    echo "-h, --help                show brief help"
}

if [[ ! -d ${PYTHON_VENV_LOCATION} ]]; then
    echo "Creating virtualenv..."
    create_venv
fi

while [[ $# > 0 ]]
do
    key="$1"
    case $key in
        -h|--help)
            help_info
            exit 1
            ;;
        *)
            help_info
            exit 1
            ;;
    esac
    shift
done
