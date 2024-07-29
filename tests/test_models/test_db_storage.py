#!/usr/bin/python3
"""Test cases for the DB_Storage class."""
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


class TestDBStorage(unittest.TestCase):
    """ Class to test the DBStorage method """

    def setUp(self):
        """ Set up test environment """
        self.storage = DBStorage()
        self.storage.reload()
        self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                    format(getenv('HBNB_MYSQL_USER'),
                                           getenv('HBNB_MYSQL_PWD'),
                                           getenv('HBNB_MYSQL_HOST'),
                                           getenv('HBNB_MYSQL_DB')))
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        """ Tear down test environment """
        self.session.close()
        self.storage.close()

    def test_all(self):
        """ Test that all returns a dictionary of all objects """
        new_user = User(email="test@test.com", password="test")
        self.storage.new(new_user)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIn("User." + new_user.id, all_objs)

    def test_new(self):
        """ Test that new adds an object to the session """
        new_user = User(email="test@test.com", password="test")
        self.storage.new(new_user)
        self.assertIn(new_user, self.session.new)

    def test_save(self):
        """ Test that save commits changes to the database """
        new_user = User(email="test@test.com", password="test")
        self.storage.new(new_user)
        self.storage.save()
        self.assertIn(new_user, self.session)

    def test_delete(self):
        """ Test that delete removes an object from the session """
        new_user = User(email="test@test.com", password="test")
        self.storage.new(new_user)
        self.storage.save()
        self.storage.delete(new_user)
        self.storage.save()
        self.assertNotIn(new_user, self.storage.all().values())

    def test_reload(self):
        """ Test that reload initializes the session correctly """
        self.storage.reload()
        self.assertIsNotNone(self.storage._DBStorage__session)

    def test_close(self):
        """ Test that close removes the session """
        self.storage.close()
        self.assertIsNone(self.storage._DBStorage__session)


if __name__ == "__main__":
    unittest.main()
