#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json

items = []

def custom_walk(directory_path):
	try:
		# 获取该路径下的所有文件和文件夹
		entries = os.listdir(directory_path)
	except FileNotFoundError:
		print(f"路径不存在: {directory_path}")
		return
	except PermissionError:
		print(f"没有权限访问: {directory_path}")
		return
	for entry in entries:
		item = {}
		full_path = os.path.join(directory_path, entry)
		# 判断是否是文件夹
		if os.path.isdir(full_path):
			item['title'] = full_path
			item['path'] = full_path
			items.append(item)
			# 递归调用 custom_walk 处理子文件夹
			custom_walk(full_path)
		else:
			item = {}
			item['title'] = full_path
			item['path'] = full_path
			items.append(item)

# Note: The first argument is the script's path
if sys.argv[1] == "":
	item = {}
	item['title'] = "Please provide the folders to be tiled"
	items.append(item)
else:
	for arg in sys.argv[1:]:
		# Check if the path is a folder
		if os.path.isdir(arg):
			custom_walk(arg)

		else:
			item = {}
			item['title'] = arg
			item['path'] = arg
			items.append(item)

print(json.dumps(items))