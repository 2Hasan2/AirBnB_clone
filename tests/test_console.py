#!/usr/bin/python3
"""Unittests for the console module.

Unittests:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing the console prompt."""

    def test_prompt_string(self):
        """Test the prompt string."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == '__main__':
    unittest.main()
