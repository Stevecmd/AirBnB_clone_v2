#!/usr/bin/python3
""" holds User class """

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


"""
This module defines a class User that inherits from BaseModel and Base
"""


storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", back_populates="user")
        reviews = relationship("Review", back_populates="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if storage_type != 'db':
            self.email = kwargs.get('email', '')
            self.password = kwargs.get('password', '')
            self.first_name = kwargs.get('first_name', '')
            self.last_name = kwargs.get('last_name', '')
        else:
            self.password = kwargs.get('password', '')
            self.email = kwargs.get('email', '')
            self.first_name = kwargs.get('first_name', '')
            self.last_name = kwargs.get('last_name', '')
