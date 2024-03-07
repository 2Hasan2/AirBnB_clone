#!/bin/bash

find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.py" -exec chmod +x {} +
rm -rf ./file.json
pycodestyle --max-line-length=120 --ignore=E402,E501,E731,W503,W504,W605 ./**/*.py 
