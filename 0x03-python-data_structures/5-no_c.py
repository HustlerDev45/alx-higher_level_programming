#!/usr/bin/env python3
def no_c(my_string):
    n_string = my.string.translate({ord(n): None for n in 'cC'})
    return n_string
