#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'cities'
    __table_args__ = {'extend_existing': True}

    if models.storage_type == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="city")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Custom string representation of the City object"""
        return "[City] ({}) {}".format(self.id, {
            'name': self.name,
            'id': self.id,
            'state_id': self.state_id,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        })
