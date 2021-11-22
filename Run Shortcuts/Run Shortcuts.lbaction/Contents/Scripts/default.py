#coding:utf-8
#!/usr/bin/env python
#
# LaunchBar Action Script
#

import sys
import json
import subprocess as sp
import os
import re

my_env = os.environ.copy()

items = []

arg = sys.argv[1]
arg = ".*" + arg.replace(" ", ".*") + ".*"
s = sp.check_output('shortcuts list', shell=True)
#s=s.decode('utf-8')
sShortcuts = sp.check_output('echo "' + s + '" | grep -iE "' + arg + '"', shell=True)
sShortcuts = sShortcuts.splitlines()
if sShortcuts[0] == "":
    item = {}
    item['title'] = "Found nothing!"
    items.append(item)
else:
    for sShortcut in sShortcuts:
        item = {}
        item['title'] = sShortcut
        item['action'] = "run.py"
        item['actionArgument'] = sShortcut
        item['actionRunsInBackground'] = True
        items.append(item)

print(json.dumps(items))