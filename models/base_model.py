#!/usr/bin/python3
"""Defines the BaseModel class. """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """update to the current time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary of the BaseModel instance"""
        ThisDict = self.__dict__.copy()
        ThisDict["created_at"] = self.created_at.isoformat()
        ThisDict["updated_at"] = self.updated_at.isoformat()
        ThisDict["__class__"] = self.__class__.__name__
        return ThisDict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    @classmethod
    def all(cls, *args):
        """returns a dictionary of all instances"""
        return models.storage.getObjList(cls.__name__)

    @classmethod
    def create(cls, *args, **kwargs):
        """creates a new instance of a class"""
        newObj = cls(*args, **kwargs)
        newObj.save()
        return newObj.id

    @classmethod
    def count(cls, *args):
        """returns the number of instances of a class"""
        return len(models.storage.getObjList(cls.__name__))

    @classmethod
    def show(cls, ObjId=""):
        """returns the instance of a class"""
        return models.storage.getObj(cls.__name__, ObjId)

    @classmethod
    def destroy(cls, ObjId=""):
        """deletes the instance of a class"""
        models.storage.deleteObj(cls.__name__, ObjId)

    @classmethod
    def update(cls, ObjId="", *args):
        models.storage.updateObj(cls.__name__, ObjId, *args)
