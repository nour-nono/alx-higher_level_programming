#!/usr/bin/python3
"""
This script manages a list of items stored in a JSON file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

ls = []
try:
    ls.extend(load_from_json_file("add_item.json"))
except Exception:
    pass

    ls.extend(sys.argv[1:])
    save_to_json_file(ls, "add_item.json")
