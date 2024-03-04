#!/bin/bash
nodemon --quiet --exec "clear && pycodestyle $1" -e py
