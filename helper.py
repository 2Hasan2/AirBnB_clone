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


if __name__ == "__main__":
    # test = "BaseModel.all()"
    # print(parse_argument(test)) # ['BaseModel', '.all()']
    # test = "City"
    # print(parse_argument(test))  # ['BaseModel']
    # test = "BaseModel.show()"
    # print(parse_argument(test)) # ['BaseModel', '.show()']
    # test = "BaseModel.show(123)"
    # print(parse_argument(test))  # ['BaseModel', '.show(123)']
    # test = "create BaseModel"
    # print(parse_argument(test))  # ['create', 'BaseModel']

    # test = 'User.update("38f22813-2753-4d42-b37c-57a17f1e4f88",
    # "first_name", "John")'
    # print(parse_argument(test))

    # test = "update City a98a18ec-0adc-4e48-b166-ee2f52202f9d hasan king"
    # print(parse_argument(test))

    # test = 'update City 50fa6556-3a40-4f00-8453-183e9f1af2c1 hasan
    # "king of the world"'

    # print(parse_argument(test))

    # test = 'City.update("a98a18ec-0adc-4e48-b166-ee2f52202f9d",
    # "hasan","king of the world")'
    # print(parse_argument(test))

    # ['create', 'all', 'show', 'EOF', 'update', 'destroy', 'count']
    # CommandsOf(HBNBCommand))
    pass
