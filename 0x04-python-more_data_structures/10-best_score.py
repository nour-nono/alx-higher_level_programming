#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    a = max(a_dictionary.values())
    for x in a_dictionary.keys():
        if a == a_dictionary[x]:
            a = x
            break
    return a
