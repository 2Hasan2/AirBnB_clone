#!/usr/bin/python3
from shlex import split
import re
import json

def parse(line: str):
    """Parses the line into a list of strings."""
    match = re.search(r'{.*}', line)
    name = ""

    # remove it from the line
    line = re.sub(r'{.*}', '', line)
    if match:
        match = match.group()
        try:
            name = json.loads(match)
        except Exception:
            return

    args = split(line)
    if name:
        args.append(name)
    return args
