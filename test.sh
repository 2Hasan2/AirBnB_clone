#!/bin/bash

python3 -m unittest discover -s tests
find . -type d -name "__pycache__" -exec rm -rf {} +
