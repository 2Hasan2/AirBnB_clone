#!/bin/bash
find tests -type d -exec bash -c 'cd {} && python3 -m unittest discover' \;
