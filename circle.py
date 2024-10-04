import math


def area(r):
    """
    Calculates the area of a circle.

    Args:
        r (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter of a circle.

    Args:
        r (float): The radius of the circle.

    Returns:
        float: The perimeter of the circle.
    """
    return 2 * math.pi * r
