#!/usr/bin/python3
def magic_string(n):
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ", ".join(["BestSchool"] * (getattr(magic_string, 'n', 0) + 1))
