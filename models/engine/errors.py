#!/usr/bin/python3
"""defines the exceptions for the project"""


class ModelNotFoundError(Exception):
    """Raised when an unknown model is passed"""
    def __init__(self):
        super().__init__(f"** class doesn't exist **")


class InstanceNotFoundError(Exception):
    """Raised when an unknown instance is passed"""

    def __init__(self):
        super().__init__(
                f"** no instance found **")


class InvalidCommandError(Exception):
    """Raised when an unknown command is passed"""
    def __init__(self):
        super().__init__(f"** command not found **")
