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

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
