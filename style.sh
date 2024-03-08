#!/bin/bash


find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.py" -exec chmod +x {} +
find . -type f -name "*.py" -exec pycodestyle {} +
rm -rf ./file.json
