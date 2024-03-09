#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
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
import console
import json
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(self.typing.__doc__) >= 1)

    def test_docstrings_in_test_console(self):
        """Test docstrings exist in test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    def test_prompt_string(self):
        """Test that the prompt string is '(hbnb) '."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Test that an empty line does not return anything."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())
