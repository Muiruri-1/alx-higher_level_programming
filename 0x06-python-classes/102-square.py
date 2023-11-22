#!/usr/bin/python3
class Square:
    """
    Defines a square with a private instance attribute 'size'
    and methods to get, set, and calculate the area of the square.
    It also implements comparison operators based on the square area.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with an optional 'size' parameter.
        The 'size' parameter must be a number (int or float)
        and cannot be less than 0
        Raises TypeError if 'size' is not a number
        or ValueError if 'size' is less than 0.
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Gets the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        The 'value' must be a number (int or float)
        and cannot be less than 0.
        Raises TypeError if 'value' is not a number
        or ValueError if 'value' is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Compares two squares based on their area.
        Returns True if the areas are equal, False otherwise.
        Raises TypeError if 'other' is not a Square object.
        """
        if not isinstance(other, Square):
            return False
        return self.__size == other.__size

    def __ne__(self, other):
        """
        Compares two squares based on their area.
        Returns True if the areas are not equal, False otherwise.
        Raises TypeError if 'other' is not a Square object.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compares two squares based on their area.
        Returns True if the current square's area is
        greater than 'other's area, False otherwise.
        Raises TypeError if 'other' is not a Square object.
        """
        if not isinstance(other, Square):
            raise TypeError("cannot compare a Square to a non-Square")
        return self.__size > other.__size

    def __ge__(self, other):
        """
        Compares two squares based on their area.
        Returns True if the current square's area is
        greater than or equal to 'other's area, False otherwise.
        Raises TypeError if 'other' is not a Square object.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Compares two squares based on their area.
        Returns True if the current square's area is less
        than 'other's area, False otherwise.
        Raises TypeError if 'other' is not a Square object.
        """
        if not isinstance(other, Square):
            raise TypeError("cannot compare a Square to a non-Square")
        return self.__size < other.__size

    def __le__(self, other):
        """
        Compares two squares based on their area.
        Returns True if the current square's area is
        less than or equal to 'other's area, False otherwise.
        Raises TypeError if 'other' is not a Square object.
        """
        return self.__lt__(other) or self.__eq__(other)
