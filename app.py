## this compiler  builds the libs for gcc automatically
##
## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license
 
import os
import re
import subprocess
import shlex
import sys
import tempfile
import shutil
import time
import traceback
## build a print statement that gets the gcc compiler and then a selected option in a file menu to grab files and compile them automaticly on point
 ## call the gcc compiler
 ## activate codderunner
 
## ask the user for the file to compile
file = input("Enter the file to compile: ")
## ask the folder where you want to compile to
folder = input("Enter the folder to compile to: ")
## ask the user for the name of the executable
executable = input("Enter the name of the executable: "),  ## enter the name of the output .c 
#### generate the executable
#os.system("gcc -o " + executable + " " + file)
## compile the file with gcc
os.system("gcc -o " + executable + " " + file)
# display a error if there is no executable to compile
if os.path.isfile(executable) == False:
    print("Error: No executable generated")
    sys.exit()
## this compiler  builds the libs for gcc automatically
