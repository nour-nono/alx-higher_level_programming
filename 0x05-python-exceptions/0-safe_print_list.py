#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    if my_list is None:
        return
    if type(my_list) is int:
        print(my_list)
        return 1
    for y in my_list:
        if z >= x:
            print()
            return z
        print(y, end="")
        z += 1
    print()
    return z
