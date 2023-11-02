#!/usr/bin/env python
import json
import random
import subprocess
import time

import os.path

pidof = subprocess.run(["pidof", "swaybg"], capture_output=True)
pids = None
if pidof.returncode == 0:
    pids = pidof.stdout[:-1]

file = "~/.config/sway/backgrounds.json"
if not os.path.isfile(os.path.expanduser(file)):
    print("Config file “{}” not found".format(file))
    exit(1)

with open(os.path.expanduser(file)) as config_file:
    config = json.load(config_file)

cmd=["swaybg"]
for item in config:
    output = config[item]
    background = output[random.randrange(len(output))]
    cmd.extend(["-o", item, "-i", os.path.expanduser(background["file"])])
    if "transform" in background:
        cmd.extend(["-m", background["transform"]])
    else:
        cmd.extend(["-m", "center"])
    if "colour" in background:
        cmd.extend(["-c", background["colour"]])
    else: cmd.extend(["-c", "#000000"])

# avoid ugly flickering by
# 1. running new `swaybg`
# 2. waiting!
# 3. killing old `swaybg`(s)
subprocess.Popen(cmd)
time.sleep(1)
if pids is not None:
    for pid in pids.split():
        subprocess.run(["kill", pid])
