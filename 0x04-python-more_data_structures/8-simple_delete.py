#!/usr/bin/python3
from tempfile import tempdir


def simple_delete(a_dictionary, key=""):
    temp = dict()
    for m in a_dictionary:
        if m != key:
            temp[m] = a_dictionary[m]
    return temp
