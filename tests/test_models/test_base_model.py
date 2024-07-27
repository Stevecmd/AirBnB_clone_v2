#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models import storage
import unittest
import datetime
from uuid import UUID
import json
import os
import models


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up for the tests"""
        self.value = BaseModel
        
        if hasattr(storage, 'storage_t') and storage.storage_t == 'db':
            from sqlalchemy import create_engine
            from sqlalchemy.orm import scoped_session, sessionmaker

            self.engine = create_engine('sqlite:///:memory:', echo=False)
            self.Session = scoped_session(sessionmaker(bind=self.engine))
            Base.metadata.create_all(self.engine)
            storage._DBStorage__session = self.Session

    def tearDown(self):
        """Tear down method for tests"""
        from models import storage
        
        if hasattr(storage, 'storage_t') and storage.storage_t == 'db':
            Base.metadata.drop_all(self.engine)
            storage._DBStorage__session.remove()
            storage._DBStorage__session = None
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default instantiation"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
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
        storage_type = os.getenv('HBNB_TYPE_STORAGE')
        if storage_type == 'file':
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())
        else:
            db_session = getattr(models.storage, '_DBStorage__session', None)
            if db_session:
                db_obj = db_session.query(BaseModel).filter_by(id=i.id).first()
                self.assertIsNotNone(db_obj)


    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(i.__class__.__name__, i.id, i.__dict__))

    def test_key_format(self):
        """ Key is properly formatted """
        # Create and add a new BaseModel object to the storage
        new = BaseModel()
        storage.new(new)
        storage.save()

        # Retrieve the ID from the newly created object
        _id = new.to_dict()['id']

        # Retrieve all keys from the storage
        keys = list(storage.all().keys())

        # Ensure that at least one key exists in storage
        self.assertGreater(len(keys), 0, "No keys found in storage")

        # Check the format of the first key
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
