#!/usr/bin/python3
import re
from shlex import split


def parse_argument(arg):
    """Parses the argument into a list of strings."""
    parentheses = re.search(r"\(.*?\)", arg)
    if parentheses:
        # handle <class>.<method>(.....)
        ClsMethod = " ".join(split(arg[:parentheses.span()[0]])).split('.')
        ClsMethod.reverse()
        line = ClsMethod + HandelParentheses(parentheses.group())
        line = [HandleMultipleWord(word) for word in line]
        return line
    else:
        # handle <method> <class> .....
        line = [HandleMultipleWord(word) for word in split(arg)]
        return line

def parse(line: str):
    """Parses the line into a list of strings."""
    args = split(line)
    return args, len(args)


def HandelParentheses(arg):
    """HandelParentheses."""
    pattern = r'"([^"]+)"|(\w+(?:\s+\w+)*)'
    matches = re.findall(pattern, arg)
    return [match[0] or f'"{match[1]}"' for match in matches]


def HandleMultipleWord(Str):
    """HandleMultipleWord"""
    words = Str.split()
    if len(words) > 1:
        return f'"{Str}"'
    else:
        return Str


def CommandsOf(cls):
    """Returns the list of methods of a class."""
    return [method.replace("do_", "")
            for method in dir(cls)
            if callable(getattr(cls, method))
            and method.startswith("do_")]
