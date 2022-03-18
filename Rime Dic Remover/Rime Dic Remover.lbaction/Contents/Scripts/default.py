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
    sSnippets = sp.check_output('tail -n 5 /Users/min/Library/Rime/custom_phrase.txt', shell=True)
    sSnippets = str(sSnippets.decode('utf-8')).split("\n")
    for sSnippet in sSnippets:
        item = {}
        item['title'] = sSnippet
        item['action'] = "remove.py"
        item['actionArgument'] = sSnippet
        item['actionRunsInBackground'] = True
        items.append(item)
else:
    for arg in sys.argv[1:]:
        arg = ".*" + arg.replace(" ", ".*") + ".*"    
        sSnippets = sp.check_output('cat /Users/min/Library/Rime/custom_phrase.txt | grep -e '+arg, shell=True)
        sSnippets = str(sSnippets.decode('utf-8')).split("\n")
        if sSnippets[0] == "":
            item = {}
            item['title'] = "Found nothing!"
            items.append(item)
        else:
            for sSnippet in sSnippets:
                item = {}
                item['title'] = sSnippet
                item['action'] = "remove.py"
                item['actionArgument'] = arg
                item['actionRunsInBackground'] = True
                items.append(item)
            
print(json.dumps(items))