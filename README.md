# AirBnB Clone

## Description
This project is a simplified version of the AirBnB web application, focusing on the development of a command-line interpreter (CLI) that can manage objects within the application.


## Environment

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)

## Command Interpreter
The command interpreter allows users to interact with the AirBnB clone from the command line. It supports various commands for managing objects such as creating, deleting, updating, and displaying instances of classes.

### How to Start
To start the command interpreter, follow these steps:
1. Clone the repository to your local machine.
```bash
git clone https://github.com/aysuarex/AirBnB_clone.git
```

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
- Ifonll (ghariebm762@gmail.com)

## run and watch use nodemon for pycodestyle
```sh
nodemon --exec "clear && pycodestyle consonsole.py" -e py
```
