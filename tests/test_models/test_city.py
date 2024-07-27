#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test class for City model"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test if state_id attribute of City is a string"""
        new = self.value()
        new.state_id = "0001"
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test if name attribute of City is a string"""
        new = self.value()
        new.name = "San Francisco"
        self.assertEqual(type(new.name), str)
