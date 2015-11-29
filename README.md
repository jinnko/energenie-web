Quick start
===========

    sudo apt-get install build-essential python python-dev python-virtualenv
    virtualenv .venv
    ln -s .venv/bin/activate
    source activate
    pip install flask energenie
    ./energenie-web.py

    wget 'https://github.com/twbs/bootstrap/releases/download/v3.3.6/bootstrap-3.3.6-dist.zip'
    unzip bootstrap-3.3.6-dist.zip
    
    
GPIO Permissions ================

To use this as the non-root user:

    sudo chgrp -R dialout /sys/class/gpio
    sudo chmod -R g+rw /sys/class/gpio
