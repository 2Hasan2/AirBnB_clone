#!/usr/bin/python3
"""defines the exceptions for the project"""


class ModelNotFoundError(Exception):
    """Raised when an unknown model is passed"""

    def __init__(self):
        """initializes the error"""
        super().__init__(f"** class doesn't exist **")


class ModelIsMissingError(Exception):
    """Raised when a model is missing"""

    def __init__(self):
        """initializes the error"""
        super().__init__(f"** class name missing **")


class InstanceNotFoundError(Exception):
    """Raised when an unknown instance is passed"""

    def __init__(self):
        """initializes the error"""
        super().__init__(f"** no instance found **")


class InvalidCommandError(Exception):
    """Raised when an unknown command is passed"""

    def __init__(self):
        super().__init__(f"** command not found **")


class IdIsMissingError(Exception):
    """Raised when an id is missing"""

    def __init__(self):
        super().__init__(f"** instance id missing **")


class AttributeIsMissingError(Exception):
    """Raised when an attribute is missing"""

    def __init__(self):
        super().__init__(f"** attribute name missing **")


class ValueIsMissingError(Exception):
    """Raised when a value is missing"""

    def __init__(self):
        super().__init__(f"** value missing **")


class InvalidSyntaxError(Exception):
    """Raised when an invalid syntax is passed"""

    def __init__(self):
        super().__init__(f"** command not found **")


def HandelError(e):
    """handles the error"""
    if isinstance(e, (
        ModelNotFoundError,
        ModelIsMissingError,
        InstanceNotFoundError,
        InvalidCommandError,
        IdIsMissingError,
        AttributeIsMissingError,
        ValueIsMissingError,
        InvalidSyntaxError
    )):
        print(e)
    else:
        print("** command not found **")
