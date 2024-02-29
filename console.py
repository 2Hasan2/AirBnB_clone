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
			"all": self.do_all,
			"show": self.do_show,
			"destroy": self.do_destroy,
			"count": self.do_count,
			"update": self.do_update
		};
		print(arg)


	def do_quit(self, arg):
		"""Qiut command to exit the program."""

	def do_EOF(self, arg):
		"""EOF command to exit the program."""

	def do_create(self, arg):
		"""Usage: create <class>
		Create a new instance of a given class.
		"""

	def do_show(self, arg):
		"""Usage: show <class> <id> or <class>.show(<id>)
		Display a string representation of a class instance of a given id.
		"""

	def do_destroy(self, arg):
		"""Usage: destroy <class> <id> or <class>.destroy(<id>)
		Delete a class instance of a given id."""

	def do_all(self, arg):
		"""Usage: all or all <class> or <class>.all()
		Display a string representation of all instances of a given class."""
		

	def do_count(self, arg):
		"""Usage: count <class> or <class>.count()
		Count the number of instances of a given class."""

	def do_update(self, arg):
		"""Usage: update <class> <id> <attribute_name> <attribute_value> or
	   <class>.update(<id>, <attribute_name>, <attribute_value>) or
	   <class>.update(<id>, <dictionary>)
	   Update an instance of a given class by adding or updating an attribute."""


if __name__ == "__main__":
	Console().cmdloop()