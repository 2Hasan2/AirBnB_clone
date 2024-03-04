#!/usr/bin/python3
"""file_storage module"""
import json
from models.base_model import BaseModel


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        pass

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        pass

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        pass

    def reload(self):
        """deserializes the JSON file to __objects"""
        pass
