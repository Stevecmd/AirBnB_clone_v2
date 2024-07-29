#!/usr/bin/python3
""" """
import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class test_Amenity(TestBaseModel):
    """Test class for Amenity model"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test if name attribute of Amenity is a string"""
        new = self.value()
        new.name = "Pool"
        self.assertEqual(type(new.name), str)
