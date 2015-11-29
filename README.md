A basic web interface to issue commands via a [Pi-mote control
board](https://energenie4u.co.uk/catalogue/product/ENER314) to switch Energenie sockets on and off.

Quick start
===========

This has been tested on Raspbian wheezy only, but should work on any distribution once you have the equivalent of the build environment working.

    sudo apt-get install build-essential git python python-dev python-virtualenv

Clone the repository.

    git clone https://github.com/jinnko/energenie-web.git
    
Set up the dependencies.

    cd energenie-web
    virtualenv .venv
    ln -s .venv/bin/activate
    source activate
    pip install flask energenie

Activate the local virtualenv.

    source activate

Run the web server.  Unfortunately this must be run as `root` due to limitations with GPIO access.

    sudo python ./energenie-web.py

Get switching on and off by pointing your browser at **http://localhost:5000/** or wherever you're running the app.
