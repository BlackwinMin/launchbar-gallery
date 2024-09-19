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
		item['badge'] = os.path.splitext(arg)[1].lower()
		items.append(item)

sorted_items = sorted(items, key=lambda x: x['badge'])

print(json.dumps(sorted_items))