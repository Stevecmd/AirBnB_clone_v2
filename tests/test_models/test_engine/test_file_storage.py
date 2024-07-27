#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        pass

    def test_new(self):
        """ New object is correctly added to __objects """
        pass

    def test_all(self):
        """ __objects is properly returned """
        pass

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        pass

    def test_empty(self):
        """ Data is saved to file """
        pass

    def test_save(self):
        """ FileStorage save method """
        pass

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        pass

    def test_reload_empty(self):
        """ Load from an empty file """
        pass

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        pass

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        pass

    def test_type_path(self):
        """ Confirm __file_path is string """
        pass

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        pass

    def test_key_format(self):
        """ Key is properly formatted """
        pass

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        pass


if __name__ == "__main__":
    unittest.main()
