#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    mx = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > mx:
            mx = my_list[i]
    return mx
