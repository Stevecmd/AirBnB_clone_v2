#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}
    if models.storage_type == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        __tablename__ = 'reviews'
        __table_args__ = {'extend_existing': True}
        super().__init__(*args, **kwargs)
        if 'place_id' not in kwargs:
            self.place_id = ""
        if 'user_id' not in kwargs:
            self.user_id = ""
        if 'text' not in kwargs:
            self.text = ""
