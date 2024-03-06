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
        arg = parse_argument(arg)
        print(f"{arg[0]}: command not found")

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
        if not len(arg):
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in models.storage.all():
            print("** no instance found **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        elif arg[2] in ["updated_at", "created_at", "id"]:
            pass
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                setattr(models.storage.all()[key], arg[2], arg[3])
                models.storage.save()
            else:
                print("from the last else")
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
