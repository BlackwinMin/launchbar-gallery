#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
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
s = sp.check_output('cat "/Users/min/Library/Mobile Documents/iCloud~md~obsidian/Documents/X000/X000-层级编码表.md" | grep -o "\- .*\-\S*" | sed "s/- //g"', shell=True).decode("utf-8")
#s=s.decode('utf-8')
tTags = sp.check_output('echo "' + s + '" | grep -iE "' + arg + '"', shell=True)
tTags = tTags.splitlines()
if tTags[0] == "":
    item = {}
    item['title'] = "Found nothing!"
    items.append(item)
else:
    for tTag in tTags:
        tTag = tTag.decode("utf-8")
        item = {}
        item['title'] = tTag
        item['action'] = "copytag.py"
        item['actionArgument'] = tTag
        item['actionRunsInBackground'] = True
        items.append(item)

print(json.dumps(items))