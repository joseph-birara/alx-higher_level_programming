#!/usr/bin/python3
"""
File: 3-error_code.py
Description: a script that handles an HttpError
"""
from urllib import request, error
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with request.urlopen(url) as data:
                print(data.read().decode('utf-8'))
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))
