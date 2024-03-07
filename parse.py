#!/usr/bin/python3
import re


def parse_argument(argument):
    """Parses the argument into a list of strings."""
    pattern = re.compile(r'(\w+)(\.\w+\(\d*\))')
    match = pattern.match(argument)
    if match:
        return [match.group(1), match.group(2)]
    return argument.split()
