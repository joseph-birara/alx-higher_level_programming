#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = list(a_dictionary.keys())
    for m in key:
        if a_dictionary[m] == value:
            del a_dictionary[m]
    return a_dictionary
