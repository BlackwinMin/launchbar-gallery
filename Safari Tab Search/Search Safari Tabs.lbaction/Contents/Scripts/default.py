#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
from subprocess import Popen, PIPE

items = []

item = {}
item['title'] = str(len(sys.argv) - 1) + ' arguments passed'
items.append(item)

scpt = '''
    on run {_string}
        set launchbarResult to {}                        tell application "Safari"                set winlist to every window                repeat with win in winlist                    set ok to true                    try                        set tablist to every tab of win                    on error errmsg                        set ok to false                    end try                    if ok then                        repeat with t in tablist                            if _string is in (name of t as string) then                                set the end of launchbarResult to {title:name of t as string, subtitle:URL of t as string, action:"jumpTab", actionArgument:(id of win as string) & "." & (index of t as string), icon:"font-awesome:fa-link"}                            else if _string is in (URL of t as string) then                                set the end of launchbarResult to {title:name of t as string, subtitle:URL of t as string, action:"jumpTab", actionArgument:(id of win as string) & "." & (index of t as string), icon:"font-awesome:fa-link"}                            else if _string is in (text of t as string) then                                set textMatch to do shell script "export LANG=en_US.UTF-8;echo '" & (text of t as string) & "'| grep -E -o '.{0,15}" & _string & ".{0,15}' | head -n1"                                set the end of launchbarResult to {title:name of t as string, subtitle:"…" & textMatch & "…", action:"jumpTab", actionArgument:(id of win as string) & "." & (index of t as string), icon:"font-awesome:fa-link"}                            end if                        end repeat                    end if                end repeat            end tell                        return launchbarResult
    end run'''
args = [sys.argv[1]]

p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate(scpt.encode('utf-8'))
stdout.decode('utf-8')
print (p.returncode, stdout, stderr)

print json.dumps(items)
