#!/bin/bash

python3 -m unittest discover tests
python3 -m unittest discover tests/test_models
./style.sh


City.update("50fa6556-3a40-4f00-8453-183e9f1af2c1", "hasan", "king of shit")