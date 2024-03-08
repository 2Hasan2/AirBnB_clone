#!/usr/bin/python3
"""unittest for console.py


"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        self.assertTrue(self.console.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        self.console.onecmd("show BaseModel 123")
        self.assertIn("** no instance found **", mock_stdout.getvalue())

    # Add more test cases for other methods...

if __name__ == '__main__':
    unittest.main()