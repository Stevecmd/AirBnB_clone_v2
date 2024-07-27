#!/usr/bin/python3
"""Test cases for the HBNB console"""

import unittest
from console import HBNBCommand
from unittest.mock import patch, MagicMock
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test the HBNB console"""

    def setUp(self):
        """Set up test environment"""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        pass

    @patch('builtins.exit', MagicMock())
    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    @patch('builtins.exit', MagicMock())
    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_missing_class(self):
        """Test show with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_show_invalid_class(self):
        """Test show with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_missing_id(self):
        """Test show with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_show_no_instance_found(self):
        """Test show with no instance found"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel 1234-5678-9101")
            self.assertEqual(f.getvalue(), "** no instance found **\n")


if __name__ == "__main__":
    unittest.main()
