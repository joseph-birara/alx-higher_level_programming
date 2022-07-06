#!/usr/bin/python3
from tempfile import tempdir


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
