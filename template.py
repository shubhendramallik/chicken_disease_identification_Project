'''
To create a project structure, we create this python file and inside this we will be writing the logic
If we write this type of file then it's one-time effort and next time we need to have this folder structure then by implementing this we get these structure automatically.
'''


'''
We need OS package.The term "OS package" in Python typically refers to the os module, which is a standard library module providing a way to interact with the operating system. The os module allows Python programs to perform various operating system-related tasks, such as file and directory operations, process management, and environment variables.
Here are some common functionalities provided by the os module:

File and Directory Operations:

os.path: Functions for common pathname manipulations.
os.listdir(path): Returns a list of filenames in the given directory.
os.mkdir(path): Creates a new directory.
os.makedirs(path): Creates a directory and its parent directories if they don't exist.
File System Information:

os.stat(path): Returns information about a file.
os.getcwd(): Returns the current working directory.
os.chdir(path): Changes the current working directory.
Process Management:

os.system(command): Executes the command in a subshell.
os.spawn* and os.exec*: Functions for process creation and replacement.
Environment Variables:

os.environ: A dictionary containing the environment variables.
Miscellaneous:

os.name: The name of the operating system dependent module imported. For example, it is 'posix' on Unix-like systems.
os.remove(path): Removes a file.
os.rmdir(path): Removes an empty directory.
'''
import os
'''
pathlib is a module in Python's standard library introduced in Python 3.4 that provides an object-oriented interface for file system paths. It is part of the broader initiative to improve file and path manipulation in Python. The pathlib module offers a more convenient and readable way to work with file paths compared to traditional string-based approaches.

The main class in the pathlib module is Path. Instances of the Path class represent file system paths, and the class provides methods and properties for working with these paths in a platform-independent manner.
'''
from pathlib import Path
'''
In Python, the logging module provides a flexible and extensible framework for emitting log messages from programs. Logging is an essential aspect of software development, allowing developers to record and analyze information about the execution of a program. It can be useful for debugging, monitoring, and gaining insights into the behavior of an application.

The logging module includes the following key components:

Loggers:

Loggers are used to capture and categorize log messages. You can create multiple loggers to organize your logs by different parts of your application.
Loggers are hierarchical, meaning they form a tree-like structure. Loggers can have parent-child relationships, and a log message sent to a logger is propagated to its ancestors.
Handlers:

Handlers determine what happens to a log message once it has been emitted by a logger. They define where the log messages go, such as writing to a file, sending emails, printing to the console, etc.
You can attach multiple handlers to a logger to perform different actions with the log messages.
Formatters:

Formatters specify the layout of the log messages. They define how the log messages should be formatted before being output by a handler.
You can customize the format to include information like timestamps, log levels, module names, and the actual log message.
Log Levels:

Log messages are assigned a severity level, indicating their importance. The standard log levels, in increasing order of severity, are DEBUG, INFO, WARNING, ERROR, and CRITICAL.
You can set a threshold level for loggers and handlers to control which messages get processed based on their severity.
'''

import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

#We can name anything here.
project_name = "cnnClassifier"

# We are going to create a list of file or folder that we want.
list_of_files = [

# This is the first folder with name .github . In this folder we will be writing all CI / CD related command in one main.yaml file. Inside this we create a another folder name workflows.
# Inside this we will create .gitkeep .We create this because if we commit any empty folder then it will reflect in the github so we should have something in the folder.
# If we create .yaml file then we will remove this .gitkeep file.  
    ".github/workflows/.gitkeep",
# We need one src folder
#Inside src we are going to create project_name
#After that there will be one local package so we need to specify this constructor file __init__.py
    f"src/{project_name}/__init__.py",


#For example, we are importing path from pathlib package which is found in the standard python library and basically hosted in pypad.That's why it is available in our python interpreter but here we are creating a project named project_name which is a custom project so this is not available in our python interpreter. That's why we need to install it as local package, so we need to specify the constructor file.
   
# Inside this project we are going to create one another folder called components.  
# This components will be another local package folder. Inside that we are going to create another constructor file. 
    f"src/{project_name}/components/__init__.py",

# Inside this project, again we are going to create one folder called utils and inside that also we are going to create one constructor.    
    f"src/{project_name}/utils/__init__.py",

# Again we are going to create another folder called config and one constructor inside it.
    f"src/{project_name}/config/__init__.py",   

# Within this config folder, we are going to create another configuration file. It will contain all the information related configuration.   
    f"src/{project_name}/config/congiguration.py",

# Inside project , we are going to create another folder called pipeline with constructor inside it.
    f"src/{project_name}/pipeline/__init__.py",

# Another folde inside project with name entity is created with constructor in it.
    f"src/{project_name}/entity/__init__.py",   

# Another folder inside project called constants is created with constructor in it.
    f"src/{project_name}/constants/__init__.py",   

# Another folder called config is created with another folder called config.yaml.
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"      

]

# Now we can start writing logic.
# First we need to go through the list one by one 

for filepath in list_of_files:
   # We need to define the path type. We are doing this because we have give forward slash in the name of the files created. But window operating system use backward slash. So we need to handle these kinds of forward slash path.
    # With filepath inside path, it will specify the path like it is a window path instead of linux path because forward path is used in linux operating system, not in windows operating system. So this will handle this error.
    filepath = Path(filepath)
    # We need to separate the folder name and file name.
    filedir, filename = os.path.split(filepath)

    # Now we need to create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)   #With exist_ok parameter, it makes sure that the same directory won't be created again and again.
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Now we will create file too.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):    # To make sure that the file does not exist or does not contain any text or code inside it.
        with open(filepath, "w") as f:      # We just want to create file with write permission.
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")


