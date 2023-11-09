#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    b = a_dictionary.copy()
    for dic_key, dic_val in b.items():
        b[dic_key] *= 2
    return b
