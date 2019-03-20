#!/usr/bin/env python
#coding=utf-8
#
# LaunchBar Action Script
#
#inspired by https://blog.csdn.net/guijiaoba/article/details/41701801
#

import os
import sys
import json
from subprocess import call
from subprocess import Popen, PIPE

noti_title_error = "json parse error."
noti_title_nojson = "argv's length is 1, no json text input."
noti_msg_error = "请输入合法的 JSON"
noti_msg_nojson = "你输入的啥都不是啊！"
noti_cmd_error = 'display notification \"' + \
    noti_msg_error + '\" with title \"' + noti_title_error +'\"'
noti_cmd_nojson = 'display notification \"' + \
    noti_msg_nojson + '\" with title \"' + noti_title_nojson +'\"'
 
length = len(sys.argv)

if length > 1:
    try:
        cmd = 'curl -s '+str(sys.argv[1])
        search_result = os.popen(cmd)
        jsonObj = json.loads(search_result.read())
        formatJsonStr = json.dumps(jsonObj,indent=4,ensure_ascii=False,sort_keys=True)
 
        scpt = '''
            on run {clipboard_content}
                tell application "System Events"
                    set activeApp to name of first application process whose frontmost is true
                    activate
                    display dialog the ["JSON Formatted! Copy to clipboard? \n\n" & clipboard_content] buttons {"Copy", "No Thanks"} default button 1 cancel button 2
                end tell

                set result_button to button returned of result as string

                if result_button is "Copy" then
                    set the clipboard to clipboard_content
                    
                end if
            end run'''
        args = [formatJsonStr]

        p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.communicate(scpt)
    except Exception, e:
        call(["osascript", "-e", noti_cmd_error])
else :
    call(["osascript", "-e", noti_cmd_nojson])