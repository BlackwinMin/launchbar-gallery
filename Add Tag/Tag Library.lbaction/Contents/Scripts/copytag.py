#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import sys
import subprocess as sp
import os
import ast
from subprocess import Popen, PIPE

my_env = os.environ.copy()
actionArgument = sys.argv[1]
sp.check_output("echo '" + actionArgument + "'| tr -d '\n' |pbcopy", shell=True)

scpt = '''
	on run {x}
		tell application "LaunchBar" to display in notification center x with title "tag copied :D"
	end run'''
args = [actionArgument]

p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate(scpt.encode('utf-8'))
stdout.decode('utf-8')
print (p.returncode, stdout, stderr)