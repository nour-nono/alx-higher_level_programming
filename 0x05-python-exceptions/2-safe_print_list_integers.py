#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        z, zz = 0, 0
        for y in my_list:
            if zz >= x:
                print()
                return z
            zz += 1
            try:
                print("{:d}".format(y), end="")
                z += 1
            except (ValueError, TypeError):
                pass
        if zz < x:
            raise IndexError("list index out of range")
        print()
        return z
    except TypeError:
        return
