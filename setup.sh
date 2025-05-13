#!/bin/bash

set -e
sudo mkdir -p /usr/share/python-cheatsheet/data/
sudo cp ./main.py /usr/bin/pysheet
sudo cp -r ./data/* /usr/share/py-sheet/data/
