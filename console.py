#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models
from phase import parse_argument


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter.
    Attributes:
        (str):Sting - prompt for the command interpreter.
    """

    prompt = "(BNB) "

    __classes = {
        "BaseModel"
    }

    def emptyline(self):
        """emptyline method for cmd module"""
        pass

    def default(self, arg):
        """default method for cmd module"""
        print(f"{arg}: command not found")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """ this create new BaseModel"""
        arg = parse_argument(arg)
        if not len(arg):
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            models.storage.save()

    def do_show(self, arg):
        """ this create new BaseModel"""
        arg = parse_argument(arg)
        if not len(arg):
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_EOF(self, arg):
        """End of file"""
        print("")
        return True

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> <attribute value> """
        arg = parse_argument(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
