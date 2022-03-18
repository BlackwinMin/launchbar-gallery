#!/usr/local/bin/python3

import sys
import subprocess as sp
import os
import ast

my_env = os.environ.copy()
actionArgument = sys.argv[1]

sp.check_output("sed -i '' -e '/" + actionArgument + "/d' /Users/min/Library/Rime/custom_phrase.txt", shell=True)