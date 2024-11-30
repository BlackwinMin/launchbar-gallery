#!/usr/local/bin/python3

import os
import sys
import plistlib
from subprocess import Popen, PIPE

if len(sys.argv[1:]) == 0:
	prompt_scpt = '''
	set the_results to (display dialog "请输入搜索关键词" default answer "")
	set the_text to text returned of the_results
	'''
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate(prompt_scpt.encode('utf-8'))
	stdout.decode('utf-8')
	_string = str(stdout).replace("b\'","").replace("\\n'","")
else:
	_string = sys.argv[1]
	
urls = [
	"请自行填写",
	"请自行填写"
	]
	
titles  = [
	"请自行填写",
	"请自行填写"
	]
	
url_list = str(urls).replace('\'','').replace('[','').replace(']','')
title_list = str(titles).replace('\'','').replace('[','').replace(']','')

scpt = '''
	on run {_string, url_list, title_list}
		--对关键词进行 URL 编码
		do shell script "/usr/bin/python -c 'import sys, urllib; print urllib.quote(sys.argv[1])' " & quoted form of _string
		set _string to result
	
		--创建搜索引擎列表
		set old_delimiters to AppleScript's text item delimiters
		set AppleScript's text item delimiters to ","
		set title_list to every text item of title_list
		set url_list to every text item of url_list
		set AppleScript's text item delimiters to old_delimiters
		set final_list to {}
			
		--选择搜索引擎
		tell application "System Events"
			set activeApp to (name of first application process whose frontmost is true)
			activate
			choose from list title_list with title "请选择要搜索的网站" with multiple selections allowed
			if result is not false then
				set choiced_urllist to result
			else
				set choiced_urllist to title_list
			end if
		end tell
			
		repeat with i from 1 to the count of choiced_urllist
			repeat with t from 1 to the count of title_list
				if item t of title_list is item i of choiced_urllist then set the end of final_list to item t of url_list
			end repeat
		end repeat
			
		--打开网页进行搜索
		tell application "Safari"
			activate
			repeat with url_item in final_list
				set search_url to (do shell script "echo '" & url_item & "' | sed 's/'*'/'" & _string & "'/g'")
				open location search_url
			end repeat
		end tell
	end run'''
args = [_string, url_list, title_list]

p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
p.communicate(scpt.encode('utf-8'))