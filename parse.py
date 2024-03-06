#!/usr/bin/python3
import re


def parse_argument(argument):
    brackets_match = re.search(r"\[(.*?)\]", argument)
    curly_braces_match = re.search(r"\{(.*?)\}", argument)

    if curly_braces_match is None:
        if brackets_match is None:
            return [i.strip(",") for i in argument.split()]
        else:
            lexer = argument.split(argument[:brackets_match.span()[0]])
            result_list = [i.strip(",") for i in lexer]
            result_list.append(brackets_match.group())
            return result_list
    else:
        lexer = argument.split(argument[:curly_braces_match.span()[0]])
        result_list = [i.strip(",") for i in lexer]
        result_list.append(curly_braces_match.group())
        return result_list
