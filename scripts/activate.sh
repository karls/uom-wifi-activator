#!/bin/bash

set -e

cd $(dirname $0)
cd ..

python2 main.py $(pwd)

