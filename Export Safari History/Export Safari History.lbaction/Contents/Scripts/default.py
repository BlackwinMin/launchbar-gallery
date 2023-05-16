#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import sys
import json
import sqlite3
from datetime import datetime

items = []

item = {}
item['title'] = str(len(sys.argv) - 1) + ' arguments passed'
items.append(item)

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    item = {}
    item['title'] = 'Argument: ' + arg
    items.append(item)
    
    # 连接到 Safari 历史记录数据库
    conn = sqlite3.connect(arg)
    cursor = conn.cursor()
    
    # 执行 SQL 查询以获取历史记录数据
    cursor.execute('SELECT title, url, visit_time FROM history_visits left join history_items on history_visits.history_item = history_items.id')
    results = cursor.fetchall()
    
    with open(arg + '.txt', 'w') as file:
        for title, url, visit_time in results:
            
            # 将时间戳转换为日期时间
            timestamp = 978307200 + visit_time
            dt = datetime.fromtimestamp(timestamp)
            standard_time = dt.strftime('%Y-%m-%d %H:%M:%S')
            
            file.write(f'{standard_time} [{title}]({url})\n\n')
            
    # 关闭数据库连接
    conn.close()

print(json.dumps(items))