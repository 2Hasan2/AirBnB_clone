#!/bin/bash

pycodestyle --max-line-length=120 --ignore=E402,E501,E731,W503,W504,W605 $1
