#!/usr/bin/python3
import sys

args = sys.argv[1:]
count = len(args)
if count == 0:
    print("Number of arguments: 0.")
elif count == 1:
    print("Number of argument: 1:")
else:
    print("Number of arguments: {}:".format(count))

for n, arg in enumerate(args, start=1):
    print("{}: {}".format(n, arg))
