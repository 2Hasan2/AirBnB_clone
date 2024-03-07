#!/usr/bin/python3
"""Unittest for the console.py file

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
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittest for testing prompting of the console"""
    def setUp(self):
        """Set up the mock stdin and stdout"""
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Tear down the mock stdin and stdout"""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_prompt(self):
        """Test the prompt of the console"""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_quit(self):
        """Test the quit command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """Test the EOF command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            self.assertEqual(f.getvalue(), "")


class TestHBNBCommand_help(unittest.TestCase):
    """Unittest for testing the help command of the console"""
    def setUp(self):
        """Set up the mock stdin and stdout"""
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Tear down the mock stdin and stdout"""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_help(self):
        """Test the help command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertTrue(f.getvalue().startswith("Documented commands"))
            self.assertTrue(f.getvalue().endswith("quit  EOF\n"))

    def test_help_quit(self):
        """Test the help quit command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(f.getvalue(), "Quit command to exit the program\n")

    def test_help_EOF(self):
        """Test the help EOF command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(f.getvalue(), "End of file\n")

    def test_help_create(self):
        """Test the help create command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(f.getvalue(), "this create new BaseModel\n")

    def test_help_show(self):
        """Test the help show command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(f.getvalue(), "this create new BaseModel\n")

    def test_help_all(self):
        """Test the help all command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(f.getvalue(), "Usage: all <class name>\n")

    def test_help_destroy(self):
        """Test the help destroy command of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(f.getvalue(), "Usage: destroy <class name> <id>\n")


if __name__ == "__main__":
    unittest.main()
