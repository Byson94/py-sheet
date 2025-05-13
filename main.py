#!/usr/bin/env python3

import argparse
import json
import os
import sys
from rich.console import Console
from rich.markdown import Markdown
from rich.columns import Columns
from rich.panel import Panel
version = "1.1"

# rich
console = Console()

# argparse
parser = argparse.ArgumentParser()

# args
parser.add_argument("-v", "--version", help="Logs the current version", action="store_true")
parser.add_argument("-m", "--manual", help="Shows the manual of a specific syntax")

args = parser.parse_args()

# this should hold the path to the directory that contains the data folder
SHARE_PATH = "/usr/share/py-sheet/data"
LOCAL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
data_folder = SHARE_PATH if os.path.exists(SHARE_PATH) else LOCAL_PATH

# results
if args.version:
    print(version)

if args.manual:
    # the args.log outputs what we entered after it
    file_path = os.path.join(data_folder, args.manual)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            console.print(Markdown(file.read()))
    else:
        console.print("ERROR: Page not found.", style="bold red")

# no arguments provided
def listAllData():
    filenames = []

    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)
        if os.path.isfile(file_path):
            filenames.append(filename)

    panels = [Panel(name, expand=True) for name in filenames]
    console.print("All cheatsheet available in the database:", style="bold")
    console.print(Columns(panels))
    console.print("Run this command with the argument '--log <cheatsheet-name>' to view the cheatsheet.")

if len(sys.argv) == 1:
    listAllData()
    sys.exit(1)