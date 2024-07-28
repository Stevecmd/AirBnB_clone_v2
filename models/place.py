#!/usr/bin/python
""" holds class City"""
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'places'
    if models.storage_type == "db":
        name = Column(String(128), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        # Define relationships
        user = relationship("User", back_populates="places")
        city = relationship("City", back_populates="places")
        state = relationship("State", back_populates="places")
        reviews = relationship("Review", back_populates="place")
    else:
        name = ""
        user_id = ""
        city_id = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)
