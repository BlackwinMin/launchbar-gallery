#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json
import sqlite3
import subprocess

def get_finder_window_titles():
    applescript = """
    tell application "Finder"
		set windowTitles to {}
		set finderWindows to every Finder window
		repeat with finderWindow in finderWindows
			set end of windowTitles to name of finderWindow
		end repeat
	end tell
	return windowTitles
    """
    
    process = subprocess.Popen(['osascript', '-e', applescript], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    
    if process.returncode == 0:
        return stdout.strip().split(', ')
    else:
        print("Error:", stderr)
        return []

window_titles = get_finder_window_titles()

items = []

for title in window_titles:
    temp = {}
    temp["title"] = title
    temp["path"] = title
    items.append(temp)
    
print(json.dumps(items))