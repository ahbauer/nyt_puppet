#!/bin/bash

PY_DIR = $1
OUT_DIR = $2

PY=$PY_DIR/python

$PY ./query_api.py $OUT_DIR/testout.txt
