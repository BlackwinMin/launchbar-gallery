#!/usr/local/bin/python3
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os
my_env = os.environ.copy()
items = []

# Note: The first argument is the script's path
vaults = sp.check_output('ls "[YOUR OBSIDIAN VAULTS PATH HERE]"', shell=True)
vaults = str(vaults.decode('utf-8')).split("\n")
for vault in vaults:
    if vault != "":
        item = {}
        t = "obsidian://open?vault="+vault
        item["title"] = vault
        item["icon"] = 'ObsidianTemplate.png'
        item["subtitle"] = t
        item["path"] = t
        item["actionArgument"] = t
        item['action'] = 'open.sh'
        items.append(item)
            
print(json.dumps(items))