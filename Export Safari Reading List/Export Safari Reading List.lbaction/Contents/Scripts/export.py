#!/usr/bin/env python3
#

import os
import plistlib
from subprocess import Popen, PIPE

INPUT_FILE  = os.path.join(os.environ['HOME'], 'Library/Safari/Bookmarks.plist')

with open(INPUT_FILE, 'rb') as plist_file:
	plist = plistlib.load(plist_file)

children = plist['Children']
for child in children:
	if child.get('Title', None) == 'com.apple.ReadingList':
		reading_list = child

bookmarks = reading_list['Children']

urls = (bookmark['URLString'] for bookmark in bookmarks)
titles = (bookmark['URIDictionary']['title'] for bookmark in bookmarks)

url_list_py = str(list(urls)).replace('\'','').replace('[','').replace(']','')
title_list_py = str(list(titles)).replace('\'','').replace('[','').replace(']','')

scpt = '''
	on run {title_list_py, url_list_py}
		set the date_stamp to ((the current date) as string)
		set NoteTitle to "# Safari 文章书签 " & the date_stamp
		set mdlink_list to {}

		set old_delimiters to AppleScript's text item delimiters
		set AppleScript's text item delimiters to ","
		set title_list to every text item of title_list_py
		set url_list to every text item of url_list_py
		set AppleScript's text item delimiters to old_delimiters

		tell application "System Events"
			set activeApp to name of first application process whose frontmost is true
			activate
			choose from list title_list with title "请选择要导出的 Reading List 文章" with multiple selections allowed
			if result is not false then
				set title_choice to result
			else
				set title_choice to title_list
			end if
		end tell

		-- 根据选出来的页面，创建对应的 Markdown 格式链接
		repeat with i from 1 to the count of title_choice
			repeat with t from 1 to the count of title_list
				if item t of title_list is item i of title_choice then set the end of mdlink_list to ((i as string) & ". [" & (item t of title_list) & "](" & (item t of url_list) & ")\n")
			end repeat
		end repeat

		-- 暂时把 AppleScript 默认分隔符换成回车，便于排版，排好文本内容后恢复系统分隔符
		set old_delim to AppleScript's text item delimiters
		set AppleScript's text item delimiters to return
		set mdlink_list to (NoteTitle & "\n\n" & mdlink_list) as text
		set AppleScript's text item delimiters to old_delim

		set the clipboard to mdlink_list
	end run'''
args = [title_list_py, url_list_py]

p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
p.communicate(scpt.encode('utf-8'))