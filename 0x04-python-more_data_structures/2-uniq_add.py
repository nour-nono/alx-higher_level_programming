#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    a, b = set(my_list), 0
    for x in a:
        b += x
    return b
