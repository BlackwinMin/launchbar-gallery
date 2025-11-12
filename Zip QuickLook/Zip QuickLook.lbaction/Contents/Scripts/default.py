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
zipItems = sp.check_output('PATH=$PATH:/usr/local/bin/; 7z l -ba "' + arg + '"', shell=True)
#zipItems = zipItems.splitlines()
zipItems = str(zipItems.decode('utf-8')).split("\n")
if zipItems[0] == "":
    item = {}
    item['title'] = "ZIP file is empty!"
    items.append(item)
else:
    for zipItem in zipItems:
        if zipItem and zipItem.strip() and "__MACOSX" not in zipItem:
            item = {}
            item['title'] = " ".join(zipItem.split()[5:])
            item['subtitle'] = " ".join(zipItem.split()[:4])
            item["badge"] = os.path.splitext(" ".join(zipItem.split()[5:]))[1]
            item['action'] = "7zx.py"
            item['actionArgument'] = '"' + arg + '" "' + " ".join(zipItem.split()[5:]) + '" -o"' + os.path.dirname(arg) + '"'
            item['actionRunsInBackground'] = True
            items.append(item)

sorted_items = sorted(items, key=lambda x: x['title'])

print(json.dumps(sorted_items))