#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json
from datetime import datetime

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
		item['badge'] = str(datetime.fromtimestamp(os.path.getmtime(arg)))
		items.append(item)

def parse_date(date_str):
    # 解析日期字符串到 datetime 对象
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

# 使用 sorted() 函数按 'badge' 键进行排序
sorted_items = sorted(items, key=lambda item: parse_date(item['badge']), reverse=True)

print(json.dumps(sorted_items))