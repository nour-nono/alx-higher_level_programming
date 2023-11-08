#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or key is None:
        return
    a_dictionary[key] = '' if value is None else value
    return a_dictionary
