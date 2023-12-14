#!/usr/local/bin/python3
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os
my_env = os.environ.copy()

from subprocess import Popen, PIPE

scpt = '''
    tell application "Keyboard Maestro Engine"
	set kmVar to getvariable "filePath"
	end tell'''

p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate(scpt.encode('utf-8'))
kmVar = stdout.decode('utf-8').rstrip("\n")

items = []

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    arg2 = "*" + arg.replace(" ", "*") + "*"
    files = sp.check_output('find '+kmVar+' -iname '+arg2+' | sort', shell=True)
    files = str(files.decode('utf-8')).split("\n")
    if files[0] == "":
        item1 = {}
        item1['title'] = "Nothing here, ask Google"
        item1['icon'] = "font-awesome:fa-google"
        item1["actionArgument"] = arg
        item1['action'] = 'search.sh'
        items.append(item1)
    else:
        for file in files:
            item = {}
            item['path'] = file
            item['quickLookURL'] = file
            items.append(item)
            
print(json.dumps(items))