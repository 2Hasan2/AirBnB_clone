#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

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
        argDict = {
            "create": self.do_create,
        }
        if arg in argDict.keys():
            argDict[arg]
        else:
            print(f"{arg}: command not found")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""

        return True
    
    def do_create(self, arg):
        """ this create new BaseModel"""
        if not arg:
            print("** class name missing **")
            return False
        if arg in HBNBCommand.__classes:
            newMod = BaseModel()
            newMod.save()
            print(id(arg))
        else :
            print(" ** class doesn't exist **")
    
    def do_EOF(self, arg):
        """End of file"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
