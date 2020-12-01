import sys
from shutil import copyfile

dst = sys.argv[1]

copyfile("1.1.py", dst + ".py")
open(dst + "_input.txt", "x")