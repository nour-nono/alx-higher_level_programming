#!/usr/bin/python3
def uppercase(st):
    for i in st:
        if str(i).isalpha():
            if i.islower():
                print(chr(ord(i) - 32), end="")
            else:
                print(i, end="")
        else:
            print(i, end="")
    print()
