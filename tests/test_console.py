#!/usr/bin/python3
"""Unittest for the console.py file

Unittest classes:
    TestHBNBCommand
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

classes = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review",
}


class TestHBNBCommand(unittest.TestCase):
    """Unittest for the console.py file"""

    def setUp(self):
        """Set up the environment to test the console"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Remove the file.json created"""
        try:
            os.remove("file.json")

        except FileNotFoundError:
            pass

    def test_create(self):
        """Test the create command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd(f"create BaseModel")
            self.assertTrue(len(output.getvalue()) > 0)
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create MyModel")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """Test the show command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show BaseModel")
            self.assertEqual(output.getvalue(), "** instance id missing **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show BaseModel 121212")
            self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_destroy(self):
        """Test the destroy command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(output.getvalue(), "** instance id missing **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("destroy BaseModel 121212")
            self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_all(self):
        """Test the all command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all BaseModel")
            self.assertEqual(output.getvalue(), "[]\n")

    def test_update(self):
        """Test the update command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("update BaseModel")
            self.assertEqual(output.getvalue(), "** instance id missing **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("update BaseModel 121212")
            self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_quit(self):
        """Test the quit command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test the emptyline command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("") is None)

    def test_help(self):
        """Test the help command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help quit"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help EOF"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help create"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help show"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help destroy"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help all"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help update"))

    def test_unknown_command(self):
        """Test an unknown command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("unknown"))

    def test_create_with_args(self):
        """Test the create command with arguments"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create BaseModel name=\"Holberton\" age=89")
            self.assertTrue(len(output.getvalue()) > 0)

    def test_show_with_args(self):
        """Test the show command with arguments"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show BaseModel 121212")
            self.assertEqual(output.getvalue(), "** no instance found **\n")


if __name__ == "__main__":
    unittest.main()
