#!/usr/bin/python3
"""
Contains tests for the DBStorage class
"""
import unittest
from models import storage
from models.engine.db_storage import DBStorage
from models.state import State
from os import getenv
from sqlalchemy.orm import scoped_session
import MySQLdb
import pep8


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests"""
        cls.db = MySQLdb.connect(
            user=getenv('HBNB_MYSQL_USER'),
            passwd=getenv('HBNB_MYSQL_PWD'),
            db=getenv('HBNB_MYSQL_DB'),
            host=getenv('HBNB_MYSQL_HOST')
        )
        cls.cursor = cls.db.cursor()
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test environment"""
        cls.cursor.close()
        cls.db.close()

    def setUp(self):
        """Set up a test method"""
        self.session = self.storage._DBStorage__session

    def tearDown(self):
        """Tear down a test method"""
        self.session.rollback()
        self.session.close()

    def test_pep8(self):
        """Test that db_storage.py follows PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new adds an object to the database"""
        state = State(name="California")
        self.storage.new(state)
        self.assertIn(state, self.session.new)

    def test_save(self):
        """Test that save properly saves objects to the database"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        self.cursor.execute("SELECT * FROM states WHERE id=%s", (state.id,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_delete(self):
        """Test that delete properly deletes an object from the database"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        self.storage.save()
        self.cursor.execute("SELECT * FROM states WHERE id=%s", (state.id,))
        result = self.cursor.fetchone()
        self.assertIsNone(result)

    def test_reload(self):
        """Test that reload properly reloads objects from the database"""
        self.assertIsInstance(self.storage._DBStorage__session, scoped_session)

    def test_close(self):
        """Test that close properly calls remove() on the session"""
        self.storage.close()
        self.assertIsNone(self.storage._DBStorage__session.registry())


if __name__ == "__main__":
    unittest.main()
