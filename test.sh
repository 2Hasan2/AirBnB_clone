#!/bin/bash

python3 -m unittest discover -s tests
python3 -m unittest discover -s tests/test_models
find . -type d -name "__pycache__" -exec rm -rf {} +
