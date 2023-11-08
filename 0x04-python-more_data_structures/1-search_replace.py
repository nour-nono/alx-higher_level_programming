#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or search is None or replace is None:
        return my_list
    a = list(map(lambda x: x if x != search else replace, my_list))
    return a
