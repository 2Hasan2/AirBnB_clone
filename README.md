# AirBnB Clone

## Description
This project is a simplified version of the AirBnB web application, focusing on the development of a command-line interpreter (CLI) that can manage objects within the application.

## Command Interpreter
The command interpreter allows users to interact with the AirBnB clone from the command line. It supports various commands for managing objects such as creating, deleting, updating, and displaying instances of classes.

### How to Start
To start the command interpreter, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the command `./console.py` to start the CLI.

### How to Use
Once the command interpreter is running, you can use the following commands:
- `create`: Create a new instance of a class.
- `show`: Display information about a specific instance.
- `destroy`: Delete a specific instance.
- `all`: Display information about all instances or all instances of a specific class.
- `update`: Update attributes of a specific instance.

For detailed usage instructions and command syntax, refer to the documentation or use the `help` command within the CLI.

### Examples
Here are some examples of how to use the command interpreter:
- `create User`: Create a new user instance.
- `show User 1234`: Display information about the user with ID 1234.
- `destroy Place 5678`: Delete the place with ID 5678.
- `all City`: Display information about all city instances.

## Authors
The following individuals have contributed to this project:
- 2Hasan2 (h01554176846@gmail.com)
- Ifonll ()

## run and watch use nodemon for pycodestyle
```sh
nodemon --exec "clear && pycodestyle consonsole.py" -e py
```
