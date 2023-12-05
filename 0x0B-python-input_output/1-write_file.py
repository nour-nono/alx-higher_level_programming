#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, "w") as fl:
        fl.write(text)
        return len(text)
