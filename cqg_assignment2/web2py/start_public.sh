#!/bin/bash

PYTHONPATHOLD=$PYTHONPATH
cd "`dirname "$0"`"
rm -f applications/cqg/{errors,sessions}/*
rm -f cqg_errors.log
export PYTHONPATH=applications/cqg/
python web2py.py -i 0.0.0.0 -p 8080 -a password
export PYTHONPATH=$PYTHONPATHOLD
cd - > /dev/null
