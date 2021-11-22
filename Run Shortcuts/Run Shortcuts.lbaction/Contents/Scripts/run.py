import sys
import subprocess as sp
import os
import ast

my_env = os.environ.copy()
actionArgument = sys.argv[1]
sp.check_output("shortcuts run '" + actionArgument + "'", shell=True)