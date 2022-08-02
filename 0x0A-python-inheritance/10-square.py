#!/usr/bin/python3
"""
more class base
"""


R = __import__('9-rectangle').Rectangle


class Square(R):
    """
    This class inheretes from Rectangle class.
    """
    def __init__(self, size):
        """
        This function initializes the size attribute.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
