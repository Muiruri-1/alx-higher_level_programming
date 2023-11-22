#!/usr/bin/python3
class MagicClass:
    """
    Represents a circle with a radius and methods to calculate its area and circumference.

    Attributes:
        _radius (int or float): The radius of the circle.

    Methods:
        __init__(radius: int or float): Initializes a MagicClass object with a specified radius.
        area() -> float: Calculates and returns the area of the circle.
        circumference() -> float: Calculates and returns the circumference of the circle.
    """

    def __init__(self, radius: int or float):
        """
        Initializes a MagicClass object with a specified radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self._radius = radius

    def area(self) -> float:
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self._radius ** 2 * math.pi

    def circumference(self) -> float:
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self._radius

