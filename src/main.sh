#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"




file_name="$SCRIPT_DIR/initialized.txt"


# Check if virtualenv is installed
if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv is not installed. Installing..."
    sudo apt install virtualenv
else
    echo "virtualenv is already installed."
fi


virtualenv $SCRIPT_DIR/venv

source $SCRIPT_DIR/venv/bin/activate



if [ -e "$file_name" ]; then

    echo "All deps met, initializing..."


else
    echo "Installing required deps..."

    sudo apt update


    sudo apt-get install espeak

    pip install -r requirements.txt
    pip install ipython
    pip install playsound
    pip install numpy
    pip install urwid
    pip install keyboard

    touch "$file_name"
fi






# Start Jupyter Lab in the background
python $SCRIPT_DIR/app.py


# Deactivate the virtual environment
deactivate
