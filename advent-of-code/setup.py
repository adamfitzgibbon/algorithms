import sys
import os
from shutil import copyfile

dst = sys.argv[1]
dir = "day-" + dst

os.mkdir(dir)

copyfile("template.py", f"{dir}/{dst}.1.py")
open(f"{dir}/{dst}.2.py", "x")
open(f"{dir}/input.txt", "x")