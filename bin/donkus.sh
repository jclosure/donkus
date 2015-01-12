#!/bin/bash

BINPATH=`dirname $0`
cd "$BINPATH/../"
python "./runserver.py" $@