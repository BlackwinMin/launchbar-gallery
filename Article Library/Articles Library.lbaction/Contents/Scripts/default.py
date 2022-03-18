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
pattern = re.compile('\[(.*)\]\((.*)\)')

if sys.argv[1] == "":
    aArticles = sp.check_output('tail -n 13 "/Users/min/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/articles.txt"', shell=True)
    aArticles = aArticles.splitlines()
    for aArticle in aArticles:
        aArticle=aArticle.decode("utf-8")
        f=re.search(pattern, aArticle)
        if f != None:
            item = {}
            item['title'] = f.group(1)
            item['subtitle'] = f.group(2)
            item['action'] = "openlink.py"
            item['actionArgument'] = f.group(2)
            item['actionRunsInBackground'] = True
            items.append(item)
else:
    for arg in sys.argv[1:]:
        arg = ".*" + arg.replace(" ", ".*") + ".*"    
        aArticles = sp.check_output('cat "/Users/min/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/articles.txt" | grep -iE "'+ arg + '"', shell=True)
        aArticles = aArticles.splitlines()
        if aArticles[0] == "":
            item = {}
            item['title'] = "Found nothing!"
            items.append(item)
        else:
            for aArticle in aArticles:
                aArticle=aArticle.decode("utf-8")
                f=re.search(pattern, aArticle)
                if f != None:
                    item = {}
                    item['title'] = f.group(1)
                    item['subtitle'] = f.group(2)
                    item['action'] = "openlink.py"
                    item['actionArgument'] = f.group(2)
                    item['actionRunsInBackground'] = True
                    items.append(item)

print(json.dumps(items))