#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        if not isinstance(other, Square):
            return False
        return self.__size == other.__size

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Square):
            raise TypeError("cannot compare a Square to a non-Square")
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Square):
            raise TypeError("cannot compare a Square to a non-Square")
        return self.__size < other.__size

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
