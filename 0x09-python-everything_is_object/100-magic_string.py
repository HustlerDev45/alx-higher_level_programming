#!/usr/bin/python3
def magic_string(n):
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return ",".join(["BestSchool"] * (magic_string.count + 1))
