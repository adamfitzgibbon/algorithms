import sys
import os
from shutil import copyfile

dst = sys.argv[1]
dir = "day-" + dst

os.mkdir(dir)

copyfile("1.1.py", f"{dir}/{dst}.1.py")
copyfile("1.1.py", f"{dir}/{dst}.2.py")
open(f"{dir}/{dst}_input.txt", "x")