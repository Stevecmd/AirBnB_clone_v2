#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime, timezone
import models
from os import getenv
import uuid
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time = "%Y-%m-%dT%H:%M:%S.%f"


storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == "db":
    Base = declarative_base()
else:
    Base = object


Base = declarative_base()


class BaseModel(Base):
    """The BaseModel class from which future classes will be derived"""
    __abstract__ = True
    id_column_type = String(60)

    @staticmethod
    def generate_id_default():
        return str(uuid.uuid4())
    id = Column(
        id_column_type,
        primary_key=True,
        default=generate_id_default
    )
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                created_at_str = kwargs["created_at"]
                created_at_format = '%Y-%m-%dT%H:%M:%S.%f'
                self.created_at = datetime.strptime(
                    created_at_str,
                    created_at_format
                )
            else:
                self.created_at = datetime.now(timezone.utc)
            if 'updated_at' in kwargs:
                date_str = kwargs["updated_at"]
                date_format = '%Y-%m-%dT%H:%M:%S.%f'
                self.updated_at = datetime.strptime(date_str, date_format)
            else:
                self.updated_at = datetime.now(timezone.utc)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now(timezone.utc)
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = (
            new_dict["created_at"].strftime(time)
            if "created_at" in new_dict
            else None
        )
        new_dict["updated_at"] = (
            new_dict["updated_at"].strftime(time)
            if "updated_at" in new_dict
            else None
        )
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop("_sa_instance_state", None)
        return new_dict

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)
