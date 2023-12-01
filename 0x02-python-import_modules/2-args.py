#!/usr/bin/python3
import sys

if __name__ == "__main__"

arg_count = len(sys.argv) - 1
if arg_count == 0:
    print("0 arguments:")
elif count == 1:
    print("1 argument:")
else:
    print("{}: {}".format(arg_count))
    for n in range(arg_count):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
