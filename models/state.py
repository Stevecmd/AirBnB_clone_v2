#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.city import City


class State(BaseModel, Base):
    """Representation of state"""
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}

    if getenv('HBNB_TYPE_STORAGE') == "db":
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
    else:
        id = Column(Integer, primary_key=True)
        name = Column(String(255), nullable=False)
        created_at = Column(TIMESTAMP, server_default=func.now())
        updated_at = Column(
            TIMESTAMP,
            server_default=func.now(),
            onupdate=func.now()
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

    def __str__(self):
        """Custom string representation of the State object"""
        return "[State] ({}) {}".format(self.id, {
            'name': self.name,
            'id': self.id,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        })
