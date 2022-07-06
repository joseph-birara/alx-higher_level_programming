#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = dict()
    for i in a_dictionary.keys():
        b_dictionary[i] = 2 * a_dictionary[i]
    return b_dictionary
