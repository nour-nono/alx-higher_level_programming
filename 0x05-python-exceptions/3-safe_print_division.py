#!/usr/bin/python3
def safe_print_division(a, b):
    z = None
    try:
        z = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(z))
        return z
