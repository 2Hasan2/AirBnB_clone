#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from parse import parse_argument
from colors import Color


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter.
    Attributes:
        (str):Sting - prompt for the command interpreter.
    """

    Color.disable(Color)

    # intro = f"{Color.Success}Welcome to the hbnb console!{Color.End}"

    prompt = f"{Color.Prompt}(hbnb) {Color.End}"

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    }

    def emptyline(self):
        """emptyline method for cmd module"""
        pass

    def default(self, arg):
        """default method for cmd module"""
        arg = parse_argument(arg)
        print(f"** {Color.Error}{arg[0]}: command not found{Color.End} **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """ this create new BaseModel """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Warning}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Warning}** class doesn't exist **{Color.End}")
        else:
            print(eval(arg[0])().id)
            models.storage.save()

    def do_show(self, arg):
        """ this show the object """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Warning}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Warning}** class doesn't exist **{Color.End}")
        elif len(arg) < 2:
            print(f"{Color.Warning}** instance id missing **{Color.End}")
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print(f"{Color.Warning}** no instance found **{Color.End}")

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_all(self, arg):
        """
        Usage: all <class name>
        """
        arg = parse_argument(arg)
        if not len(arg):
            print([str(models.storage.all()[key])
                   for key in models.storage.all()])
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Warning}** class doesn't exist **{Color.End}")
        else:
            print([str(models.storage.all()[key])
                   for key in models.storage.all()
                   if key.split(".")[0] == arg[0]])

    def do_destroy(self, arg):
        """Usage: destroy <class name> <id> """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Warning}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Warning}** class doesn't exist **{Color.End}")
        elif len(arg) < 2:
            print(f"{Color.Warning}** instance id missing **{Color.End}")
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print(f"{Color.Warning}** no instance found **{Color.End}")

    def do_update(self, arg):
        """
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Warning}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Warning}** class doesn't exist **{Color.End}")
        elif len(arg) < 2:
            print(f"{Color.Warning}** instance id missing **{Color.End}")
        elif "{}.{}".format(arg[0], arg[1]) not in models.storage.all():
            print(f"{Color.Warning}** no instance found **{Color.End}")
        elif len(arg) < 3:
            print(f"{Color.Warning}** attribute name missing **{Color.End}")
        elif len(arg) < 4:
            print(f"{Color.Warning}** value missing **{Color.End}")
        elif arg[2] in ["updated_at", "created_at", "id"]:
            pass
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                setattr(models.storage.all()[key], arg[2], arg[3])
                models.storage.save()
            else:
                print(f"{Color.Warning}** no instance found **{Color.End}")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
