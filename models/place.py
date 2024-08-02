#!/usr/bin/python
""" holds class Place"""
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE')

# Define the association table for the many-to-many relationship
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False
                             ),
                      Column(
                        'amenity_id', String(60),
                        ForeignKey('amenities.id'),
                        primary_key=True,
                        nullable=False)
                      )


class Place(BaseModel, Base):
    """Representation of Place """
    __tablename__ = 'places'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        description = Column(String(1024))
        # Define relationships
        user = relationship("User", back_populates="places")
        city = relationship("City", back_populates="places")
        state = relationship("State", back_populates="places")
        reviews = relationship("Review", back_populates="place")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False
            )
    else:
        name = ""
        user_id = ""
        city_id = ""
        state_id = ""
        description = ""
        amenities = []

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)
