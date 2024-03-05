#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter."""
    
    prompt = "(hbnb) "

    __classes = {
        "<class 'BaseModel'>",
        "<class 'User'>",
        "<class 'State'>",
        "<class 'City'>",
        "<class 'Amenity'>",
        "<class 'Place'>",
        "<class 'Review'>"
    }

    def emptyline(self):
        """Emptyline method for cmd module."""
        pass

    def default(self, arg):
        """Default method for cmd module."""
        argDict = {
            "quit": self.do_quit,
            "save": self.do_save,
            "new": self.do_new,
        }
        if arg in argDict.keys():
            argDict[arg]()
        else:
            print(f"{arg}: command not found")

    def do_quit(self, arg):
        """Quit command."""
        print("Exiting HBNB command prompt.")
        return True

    def do_save(self, arg):
        """Save command."""
        print("Saving data.")
        return False

    def do_new(self, arg):
        """New command."""
        print(f"Creating a new {arg}.")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
