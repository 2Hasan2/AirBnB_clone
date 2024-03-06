#!/usr/bin/python3
"""file_storage module"""
import json
from models.base_model import BaseModel
# from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f
            )

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objDict = json.load(f)
                for obj in objDict.values():
                    ClassName = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(ClassName)(**obj))
        except FileNotFoundError:
            pass
        except ValueError:
            pass
        except TypeError:
            pass
        except Exception as e:
            raise e
