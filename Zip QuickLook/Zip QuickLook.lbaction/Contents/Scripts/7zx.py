#!/usr/local/bin/python3

import sys
import subprocess as sp
import os
import ast

my_env = os.environ.copy()
actionArgument = sys.argv[1]

sp.check_output("PATH=$PATH:/usr/local/bin/; 7z x " + actionArgument, shell=True)