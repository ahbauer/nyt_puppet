#!/bin/bash

PY_DIR=$1
CODE_DIR=$2
OUT_FILE=$3

PY=$PY_DIR/python

$PY $CODE_DIR/query_api.py $OUT_FILE
