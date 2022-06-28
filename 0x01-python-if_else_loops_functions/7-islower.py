#!/usr/bin/python3
from sqlalchemy import false, true


def islower(c):
    if c >= 'a' and c <= 'z':
        return true
    else:
        return false
