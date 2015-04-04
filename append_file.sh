#!/bin/bash

PY_DIR=$1
LOG_FILE=$2
OUT_FILE=$3

PY=$PY_DIR/python

$PY ./query_api.py $LOG_FILE $OUT_FILE
