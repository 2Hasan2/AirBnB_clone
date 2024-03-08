#!/usr/bin/python3
"""file_storage module"""
import json
from .errors import *
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    models = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized = {
            key: value.to_dict()
            for key, value in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            deserialized = {}
            with open(FileStorage.__file_path) as f:
                deserialized = json.loads(f.read())
            FileStorage.__objects = {
                key: eval(value["__class__"])(**value)
                for key, value in deserialized.items()
            }
        except (FileNotFoundError, JSONDecodeError):
            pass
        except Exception as e:
            raise e

    # helper functions
    def deleteObj(self, model="", ObjId=""):
        """delete object from __objects"""
        F = FileStorage
        if model not in F.models:
            raise ModelNotFoundError()
        
        if not ObjId:
            raise IdIsMissingError()

        key = model + "." + ObjId
        if key not in F.__objects:
            raise InstanceNotFoundError()

        del F.__objects[key]
        self.save()

    def getObj(self, model="", ObjId=""):
        """get object from __objects"""
        F = FileStorage
        if model not in F.models:
            raise ModelNotFoundError()

        if not ObjId:
            raise IdIsMissingError()

        key = model + "." + ObjId
        if key not in F.__objects:
            raise InstanceNotFoundError()

        return F.__objects[key]

    def updateObj(self, model="", ObjId="", *AttAndVal):
        """update object from __objects"""
        F = FileStorage
        if model not in F.models:
            raise ModelNotFoundError()
        
        if not ObjId:
            raise IdIsMissingError()
        
        key = model + "." + ObjId
        if key not in F.__objects:
            raise InstanceNotFoundError()
        if len(AttAndVal) > 2:
            raise InvalidSyntaxError()

        if len(AttAndVal) == 0:
            raise AttributeIsMissingError()

        if len(AttAndVal) == 1:
            raise ValueIsMissingError()        

        attr, value = AttAndVal

        if  not isinstance(attr, str):
            raise InvalidSyntaxError()

        if attr in ("id", "created_at", "updated_at"):
            return

        instance = F.__objects[key]
        setattr(instance, attr, value)
        self.save()

    def getObjList(self, model=""):
        """get object list from __objects"""
        F = FileStorage
        if model == "":
            return [
                str(val)
                for val in F.__objects.values()
            ]
        elif model and model in F.models:
            results = []
            for key, val in FileStorage.__objects.items():
                if key.startswith(model):
                    results.append(str(val))
            return results
        else:
            raise ModelNotFoundError()
