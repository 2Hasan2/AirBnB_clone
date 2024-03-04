#!/usr/bin/python3
"""Defines the BaseModel class. """
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel():
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def save(self):
        """update to the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary of the BaseModel instance"""
        ThisDict = self.__dict__.copy()
        ThisDict["created_at"] = self.created_at.isoformat()
        ThisDict["update_at"] = self.updated_at.isoformat()
        ThisDict["__class__"] = self.__class__.__name__
        return ThisDict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
