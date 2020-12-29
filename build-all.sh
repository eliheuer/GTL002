#!/bin/bash
set -e

# Run from the root directory of the GTL002 Git repo
sh source/build.sh
python3 docs/drawbot/specimen-001.py
