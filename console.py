#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from helper import parse
from models.engine.errors import *


classes = storage.models


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter."""

    prompt = f"(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Override the emptyline method
        """
        pass

    def do_all(self, arg):
        """Prints all string representation of \
all instances based or not on the class name
        """
        args = parse(arg)[:1]
        try:
            print(storage.getObjList(*args))
        except Exception as e:
            HandelError(e)

    def do_show(self, arg):
        """ Print string repr of a class instance, given id
        """
        args = parse(arg)[:2]
        try:
            print(storage.getObj(*args))
        except Exception as e:
            HandelError(e)

    def do_count(self, arg):
        """ Display count of instances specified
        """
        args = parse(arg)[:1]
        try:
            print(len(storage.getObjList(*args)))
        except Exception as e:
            HandelError(e)

    def do_create(self, arg):
        """ Create instance specified by user
        """
        args = parse(arg)[:1]
        try:
            print(storage.createObj(*args))
        except Exception as e:
            HandelError(e)

    def do_destroy(self, arg):
        """Delete a class instance of a given id, save result to json file
        """
        args = parse(arg)[:2]
        try:
            storage.deleteObj(*args)
        except Exception as e:
            HandelError(e)

    def default(self, arg):
        """default method for cmd module
        """
        if "." in arg and arg[-1] == ")":
            if arg.split(".")[0] not in classes:
                print("** class doesn't exist **")
                return
            return self.class_method(arg)
        else:
            print("** command not found **")
            return

    def class_method(self, arg):
        """class method
        """
        try:
            cls = arg.split(".")[0]
            method = arg.split(".")[1].split("(")[0]
            arg = arg.split("(")[1].split(")")[0]
            out = eval(f"{cls}.{method}")(arg)
            if out:
                print(out)
        except Exception as e:
            HandelError(e)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding \
or updating attribute (save the change into the JSON file)
        """
        args = parse(arg)
        try:
            storage.updateObj(*args)
        except Exception as e:
            HandelError(e)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
