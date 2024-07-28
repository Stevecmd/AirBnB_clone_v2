#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """Representation of state"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )
    places = relationship(
        "Place",
        back_populates="state",
        cascade="all, delete-orphan"
    )

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """Getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list


# Conditional class definition for non-database storage
if getenv('HBNB_TYPE_STORAGE') != "db":
    class State(BaseModel):
        """Representation of state for file storage"""
        name = ""

        def __init__(self, *args, **kwargs):
            """Initializes state"""
            super().__init__(*args, **kwargs)

        @property
        def cities(self):
            """Getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
