#!/usr/local/bin/python3
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os

my_env = os.environ.copy()

items = []

# Note: The first argument is the script's path
if sys.argv[1] == "":
    fFiles = sp.check_output('cat "./fList.txt" | sort', shell=True)
    fFiles = str(fFiles.decode('utf-8')).split("\n")
    for fFile in fFiles:
        item = {}
        fName = sp.check_output('basename \"'+fFile+'\"', shell=True)
        fName = str(fName.decode('utf-8'))
        item['title'] = fName
        item['subtitle'] = fFile
        item['path'] = fFile
        item['icon'] = "font-awesome:fa-file-o"
        item['action'] = "open.sh"
        item['actionArgument'] = fFile
        items.append(item)
else:
    for arg in sys.argv[1:]:
        arg = ".*" + arg.replace(" ", ".*") + ".*"    
        fFiles = sp.check_output('cat "./fList.txt" | grep -e '+arg, shell=True)
        fFiles = str(fFiles.decode('utf-8')).split("\n")
        if fFiles[0] == "":
            item = {}
            item['title'] = "Found nothing!"
            items.append(item)
        else:
            for fFile in fFiles:
                item = {}
                fName = sp.check_output('basename \"'+fFile+'\"', shell=True)
                fName = str(fName.decode('utf-8'))
                item['title'] = fName
                item['subtitle'] = fFile
                item['path'] = fFile
                item['icon'] = "font-awesome:fa-file-o"
                item['action'] = "open.sh"
                item['actionArgument'] = arg
                items.append(item)
            
print(json.dumps(items))