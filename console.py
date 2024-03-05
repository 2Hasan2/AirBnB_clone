#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter.
    Attributes:
        (str):Sting - prompt for the command interpreter.
    """

    prompt = "(BNB) "

    __classes = {
        """<class 'BaseModel'>""",
        """<class 'User'>""",
        """<class 'State'>""",
        """<class 'City'>""",
        """<class 'Amenity'>""",
        """<class 'Place'>""",
        """<class 'Review'>"""
    }

    def emptyline(self):
        """emptyline method for cmd module"""
        pass

    def default(self, arg):
        """default method for cmd module"""
        argDict = {
        }
        if arg in argDict.keys():
            argDict[arg]
        else:
            print(f"{arg}: command not found")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""

        return True
    
    def do_EOF(self, arg):
        """End of file"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
