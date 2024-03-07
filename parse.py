#!/usr/bin/python3
import re


def parse_argument(arg):
    """Parses the argument into a list of strings."""
    match = re.search(r'\(.*?\)', arg)
    if match:
        arg = arg.replace(match.group(), " " + match.group())
    arg = arg.replace(".", " ")
    arg = arg.replace("(", "")
    arg = arg.replace(")", "")
    return arg.split()


def CommandsOf(cls):
    """Returns the list of methods of a class."""
    return [method.replace("do_", "")
            for method in dir(cls)
            if callable(getattr(cls, method))
            and method.startswith("do_")]


if __name__ == "__main__":
    from console import HBNBCommand
    test = "BaseModel.all()"
    print(parse_argument(test))  # ['BaseModel', '.all()']
    test = "City"
    print(parse_argument(test))  # ['BaseModel']
    test = "BaseModel.show()"
    print(parse_argument(test))  # ['BaseModel', '.show()']
    test = "BaseModel.show"
    print(parse_argument(test))  # ['BaseModel.show']
    test = "BaseModel.show(123)"
    print(parse_argument(test))  # ['BaseModel', '.show(123)']
    test = "create BaseModel"
    print(parse_argument(test))  # ['create', 'BaseModel']

    # ['create', 'all', 'show', 'EOF', 'update', 'destroy', 'count']
    print(CommandsOf(HBNBCommand))
