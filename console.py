import cmd


class Console(cmd.Cmd):
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
            "quit": self.do_quit,
            "save": self.do_save,
            "new": self.do_new,
        }
        if arg in argDict.keys():
            argDict[arg]
        else:
            print(f"{arg}: command not found")

    def do_quit(self, arg):
        print("from do_quit")
        # this true will end the program
        return True

    def do_save(self, arg):
        print("from do_save")
        return False


if __name__ == "__main__":
    Console().cmdloop()
