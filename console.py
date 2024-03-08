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
from helper import parse_argument, CommandsOf
from colors import Color


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter."""

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
        """this will handle the <class name>.method()"""
        if len(arg) > 1 and arg[1] in HBNBCommand.__classes:
            if arg[0] in CommandsOf(HBNBCommand):
                NewArg = arg[1] + " " + " ".join(arg[2:])
                eval(f"self.do_{arg[0]}('{NewArg}')")
                return False
        print(f"{Color.Yellow}** command not found **{Color.End}")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """ this create new BaseModel """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Yellow}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Yellow}** class doesn't exist **{Color.End}")
        else:
            obj = eval(arg[0])()
            print(obj.id)
            obj.save()

    def do_show(self, arg):
        """ this show the object """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Yellow}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Yellow}** class doesn't exist **{Color.End}")
        elif len(arg) < 2:
            print(f"{Color.Yellow}** instance id missing **{Color.End}")
        else:
            key = arg[0] + "." + arg[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print(f"{Color.Yellow}** no instance found **{Color.End}")

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
            print([str(storage.all()[key])
                   for key in storage.all()])
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Yellow}** class doesn't exist **{Color.End}")
        else:
            print([str(storage.all()[key])
                   for key in storage.all()
                   if key.split(".")[0] == arg[0]])

    def do_destroy(self, arg):
        """
        Usage: destroy <class name> <id>
        """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Yellow}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Yellow}** class doesn't exist **{Color.End}")
        elif len(arg) < 2:
            print(f"{Color.Yellow}** instance id missing **{Color.End}")
        else:
            key = arg[0] + "." + arg[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print(f"{Color.Yellow}** no instance found **{Color.End}")

    def do_update(self, arg):
        """
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Yellow}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Yellow}** class doesn't exist **{Color.End}")
        elif len(arg) < 2:
            print(f"{Color.Yellow}** instance id missing **{Color.End}")
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print(f"{Color.Yellow}** no instance found **{Color.End}")
        elif len(arg) < 3:
            print(f"{Color.Yellow}** attribute name missing **{Color.End}")
        elif len(arg) < 4:
            print(f"{Color.Yellow}** value missing **{Color.End}")
        elif arg[2] in ["updated_at", "created_at", "id"]:
            pass
        else:
            key = arg[0] + "." + arg[1]
            if key in storage.all():
                setattr(storage.all()[key],
                        arg[2], arg[3].replace("'", "").replace('"', ""))
                storage.save()
            else:
                print(f"{Color.Yellow}** no instance found **{Color.End}")

    def do_count(self, arg):
        """
        Usage: count <class name>
        """
        arg = parse_argument(arg)
        if not len(arg):
            print(f"{Color.Yellow}** class name missing **{Color.End}")
        elif arg[0] not in HBNBCommand.__classes:
            print(f"{Color.Yellow}** class doesn't exist **{Color.End}")
        else:
            print(len([key for key in storage.all()
                       if key.split(".")[0] == arg[0]]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
