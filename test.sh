#!/bin/bash

python3 -m unittest discover tests
python3 -m unittest discover tests/test_models
./style.sh
