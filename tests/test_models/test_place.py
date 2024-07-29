#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class test_Place(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.description), str)
        pass

    def test_number_rooms(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.number_rooms), int)
        pass

    def test_number_bathrooms(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.number_bathrooms), int)
        pass

    def test_max_guest(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.max_guest), int)
        pass

    def test_price_by_night(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.price_by_night), int)
        pass

    def test_latitude(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.latitude), float)
        pass

    def test_longitude(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.latitude), float)
        pass

    def test_amenity_ids(self):
        """ """
        # new = self.value()
        # self.assertEqual(type(new.amenity_ids), list)
        pass
