#!/bin/bash

python3 -m unittest discover -s tests
python3 -m unittest discover -s tests/test_models
./style.sh
