# Suntimes service
I couldn't find any web services that would let you retrieve sunrise/sunset times, so I've created this.
It's very specific at the moment and only offers:
 - `GET`ting the next sunrise for Bute, South Australia
 - `GET`ting the next sunset for Bute, South Australia

... but it could easily be changed to be more generic.

## Getting started

    git clone <this repo>
    cd suntimes-service/
    sudo apt-get install python-dev # installs Python.h
    virtualenv --no-site-packages -p python2.7 . # create a virtualenv
    . bin/activate
    pip install -r requirements.txt # install the requirements

## Deploying the service

    aws configure # set the correct credentials
    cd suntimes-service/
    sls deploy
