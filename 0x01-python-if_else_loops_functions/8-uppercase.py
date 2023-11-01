#!/usr/bin/python3
def uppercase(st):
    for i in st:
        if str(i).isalpha() and i.islower():
            j = chr(ord(i) - 32)
        else:
            j = i
        print("{}".format(j), end="")
    print()
