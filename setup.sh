#!/bin/bash

set -e
sudo mkdir -p /usr/share/python-cheatsheet/data/
sudo cp ./main.py /usr/bin/python-cheatsheet
sudo cp -r ./data/* /usr/share/python-cheatsheet/data/
