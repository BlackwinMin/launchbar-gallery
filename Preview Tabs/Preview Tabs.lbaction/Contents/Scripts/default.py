#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json
import sqlite3
import subprocess
import csv
from io import StringIO

def get_finder_window_titles():
    applescript = r'''
    tell application "Preview"
        set windowTitles to {}
        repeat with previewWindow in every window
            set end of windowTitles to path of document of previewWindow
        end repeat
    end tell

    set jsonItems to {}
    repeat with windowTitle in windowTitles
        set escapedTitle to my replaceText("\\", "\\\\", windowTitle as text)
        set escapedTitle to my replaceText("\"", "\\\"", escapedTitle)
        set end of jsonItems to "\"" & escapedTitle & "\""
    end repeat

    set AppleScript's text item delimiters to ","
    set jsonText to "[" & (jsonItems as text) & "]"
    set AppleScript's text item delimiters to ""
    return jsonText

    on replaceText(findText, replacementText, sourceText)
        set AppleScript's text item delimiters to findText
        set textItems to text items of sourceText
        set AppleScript's text item delimiters to replacementText
        set sourceText to textItems as text
        set AppleScript's text item delimiters to ""
        return sourceText
    end replaceText
    '''

    process = subprocess.Popen(
        ['osascript', '-e', applescript],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return json.loads(stdout)
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