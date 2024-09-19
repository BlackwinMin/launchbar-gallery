#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json

items = []

# Note: The first argument is the script's path
if sys.argv[1] == "":
	item = {}
	item['title'] = "Nothing here"
	items.append(item)
else:
	for arg in sys.argv[1:]:
		item = {}
		item['title'] = os.path.basename(arg)
		item['path'] = arg
		item['badge'] = str(os.path.getsize(arg))
		items.append(item)

def badge_to_int(item):
    return int(item['badge'])
sorted_items = sorted(items, key=badge_to_int, reverse=True)

def format_size(bytes_value):
    """将字节值转换为适当的单位（KB, MB, GB）"""
    kb_value = bytes_value / 1024
    mb_value = kb_value / 1024
    gb_value = mb_value / 1024
    
    if gb_value >= 1:
        return f"{gb_value:.2f} GB"
    elif mb_value >= 1:
        return f"{mb_value:.2f} MB"
    elif kb_value >= 1:
        return f"{kb_value:.2f} KB"
    else:
        return f"{bytes_value} bytes"

def badge_to_bytes(item):
    return int(item['badge'])

# 将 badge 键的值从文本格式转换为字节数，并格式化为适当的单位
for item in sorted_items:
    bytes_value = badge_to_bytes(item)
    item['badge'] = format_size(bytes_value)

print(json.dumps(sorted_items))