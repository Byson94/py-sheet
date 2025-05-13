#!/bin/bash

set -e
sudo mkdir -p /usr/share/py-sheet/data/
sudo cp ./main.py /usr/bin/pysheet
sudo cp -r ./data/* /usr/share/py-sheet/data/
