#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import re


items = []
pattern = re.compile('\[(.*)\]\((.*)\)(.*)')

searchInput = sys.argv[1]

if searchInput:
    keywords = searchInput.split('，')
    for kw in keywords:
        kw1 = ".*" + kw.replace(" ", ".*") + ".*"    

        try:
            aArticles = sp.check_output('cat "/Users/min/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/articles.txt" | grep -iE "'+ kw1 + '"', shell=True)
            
            aArticles = aArticles.splitlines()
            for aArticle in aArticles:
                aArticle = aArticle.decode("utf-8")
                f=re.search(pattern, aArticle)
                if f != None:
                    items.append({
                        'title': f.group(1),
                        'subtitle': f.group(2),
                        'action': 'openlink.py',
                        'actionArgument': f.group(2),
                        'badge': f.group(3),
                        'actionRunsInBackground': True,
                        'icon': 'font-awesome:fa-bookmark'
                    })
        except:
            items.append({
                'title': 'Keyword "{}" found nothing. Try another keyword.'.format(kw)
            })  

    items = [x for i, x in enumerate(items) if x not in items[:i]]  # 列表项目去重

else:
    items.append({
        'title': 'Show All Articles in the doc.',
        'path': '/Users/min/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/articles.txt'
    })    

print(json.dumps(items))