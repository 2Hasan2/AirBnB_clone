#!/usr/bin/python3
"""Defines the BaseModel class. """
import models
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """update to the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary of the BaseModel instance"""
        ThisDict = self.__dict__.copy()
        ThisDict["created_at"] = self.created_at.isoformat()
        ThisDict["update_at"] = self.updated_at.isoformat()
        ThisDict["__class__"] = self.__class__.__name__
        return ThisDict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
