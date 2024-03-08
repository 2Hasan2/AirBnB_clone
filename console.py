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
from helper import parse_argument, CommandsOf, parse
from models.engine.errors import *
import shlex


classes = storage.models

class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter."""

    prompt = f"(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True
    
    def emptyline(self):
        """Override the emptyline method"""
        pass    


    def do_all(self, arg):
        """
        Usage: all <class name>
        """
        args, n = parse(arg)
        if n < 2:
            try:
                print(storage.getObjList(*args))
            except ModelNotFoundError as e:
                print(e)
        else:
            print(f"** too many args **")

    def do_show(self, arg):
        """ this show the object """
        args , n = parse(arg)
        if not n:
            print(f"** class name missing **")
        elif n == 1:
            if args[0] not in classes:
                print(f"** class doesn't exist **")
            else:
                print(f"** instance id missing **")
        elif n == 2:
            try:
                print(storage.getObj(*args))
            except ModelNotFoundError as e:
                print(e)
            except InstanceNotFoundError as e:
                print(e)
        else:
            print(f"** command not found **")

    def do_create(self, arg):
        """ this create new BaseModel """
        args , n = parse(arg)
        if not n:
            print(f"** class name missing **")
        elif args[0] not in classes:
            print(f"** class doesn't exist **")
        elif n == 1:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)
        else:
            print(f"** command not found **")

    def do_destroy(self, arg):
        """
        Usage: destroy <class name> <id>
        """
        args, n = parse(arg)
        if not n:
            print(f"** class name missing **")
        elif n == 1:
            if args[0] not in classes:
                print(f"** class doesn't exist **")
            else:
                print(f"** instance id missing **")
        elif n == 2:
            try:
                storage.deleteObj(*args)
            except ModelNotFoundError as e:
                print(e)
            except InstanceNotFoundError as e:
                print(e)
        else:
            print(f"** too many args **")
           


    def default(self, arg):
        """default method for cmd module"""
        if "." in arg and arg[-1] == ")":
            if arg.split(".")[0] not in classes:
                print(f"** class doesn't exist **")
                return
            return self.class_method(arg)
        else:
            print(f"** command not found **")
            return


    def class_method(self, arg):
        """class method"""
        try:
            cls = arg.split(".")[0]
            method = arg.split(".")[1].split("(")[0]
            arg = arg.split("(")[1].split(")")[0]
            out = eval(f"{cls}.{method}({arg})")
            if out:
                print(out)
        except AttributeError as e:
            print(f"** method doesn't exist **")
        except ModelNotFoundError as e:
            print(e)
        except IdIsMissingError as e:
            print(e)
            pass
        except InstanceNotFoundError as e:
            print(e)
        except AttributeIsMissingError as e:
            print(e)
        except ValueIsMissingError as e:
            print(e)
        except InvalidSyntaxError as e:
            print(e)
        except Exception as e:
            print(f"** command not found **")

    
    def do_models(self, arg):
        """Prints all the models"""
        print(*classes)



    def do_update(self, arg):
        """
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args, n = parse(arg)
        try:
            storage.updateObj(*args)
        except ModelNotFoundError as e:
            print(e)
        except IdIsMissingError as e:
            print(e)
        except InstanceNotFoundError as e:
            print(e)
        except AttributeIsMissingError as e:
            print(e)
        except ValueIsMissingError as e:
            print(e)
        except InvalidSyntaxError as e:
            print(e)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
