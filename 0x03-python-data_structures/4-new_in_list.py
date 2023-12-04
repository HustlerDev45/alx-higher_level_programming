#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0 or idx > len(copy) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
