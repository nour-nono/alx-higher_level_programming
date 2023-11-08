#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for dic_key, dic_val in sorted(a_dictionary.items()):
        print(f"{dic_key}: {dic_val}")
