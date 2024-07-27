#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up for the tests"""
        pass

    def tearDown(self):
        """Tear down method for tests"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default instantiation"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instantiation with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test instantiation with invalid kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test string representation"""
        i = self.value()()
        self.assertEqual(
            str(i),
            '[{}] ({}) {}'.format(
                self.name, i.id, i.__dict__
            )
        )

    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
        storage.new(new)
        storage.save()
        _id = new.to_dict()['id']
        keys = list(storage.all().keys())
        self.assertGreater(len(keys), 0, "No keys found in storage")
        temp = keys[0]
        expected_key = 'BaseModel' + '.' + _id
        self.assertEqual(temp, expected_key)

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test that updated_at is updated on save"""
        i = self.value()
        old_updated_at = i.updated_at
        i.save()
        self.assertNotEqual(i.created_at, i.updated_at)
        self.assertNotEqual(old_updated_at, i.updated_at)
