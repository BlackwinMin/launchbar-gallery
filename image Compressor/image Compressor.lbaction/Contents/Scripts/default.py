#!/usr/local/bin/python3
#
# LaunchBar Action Script
#
import sys
import subprocess as sp
import os
import json
import shutil

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]
# Note: The first argument is the script's path

for arg in sys.argv[1:]:
        fileType = (os.path.splitext(arg)[-1]).lower()
        if fileType == ".png":
                my_command = ["pngquant", arg, "--quality", "70-95", "--ext=.png", "--force"]
                sp.check_output(my_command, env=my_env)
        elif fileType == ".jpg" or fileType == ".jpeg":
                my_command = ["jpegoptim", "-m70", "--max90", arg] 
                sp.check_output(my_command, env=my_env)
        elif fileType == ".gif":
                my_command = ["gifsicle", "-i", arg, "--optimize=3", "-o", arg] 
                sp.check_output(my_command, env=my_env)
os.system('sh noti.sh')