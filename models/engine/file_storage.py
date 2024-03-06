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
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = {
                    k: BaseModel(**v) for k, v in json.load(f).items()
                }
        except FileNotFoundError:
            pass
        except ValueError:
            pass
        except TypeError:
            pass
        except Exception as e:
            raise e
