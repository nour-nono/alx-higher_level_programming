#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return
    if key not in a_dictionary.keys() or key is None:
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary
