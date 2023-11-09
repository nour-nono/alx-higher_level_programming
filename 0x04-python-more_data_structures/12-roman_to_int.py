#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
        a_dictionary = {'M': 1000, 'D': 500, 'C': 100,
                        'L': 50, 'X': 10, 'V': 5, 'I': 1}
    roman_string = roman_string.strip().upper()
    add, sub = a_dictionary[roman_string[-1]], 0
    for x in range(len(roman_string) - 1):
        if a_dictionary[roman_string[x]] < a_dictionary[roman_string[x + 1]]:
            sub += a_dictionary[roman_string[x]]
        else:
            add += a_dictionary[roman_string[x]]
    return add - sub
