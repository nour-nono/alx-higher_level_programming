#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None and set_2 is None:
        return
    return set_1 ^ set_2
