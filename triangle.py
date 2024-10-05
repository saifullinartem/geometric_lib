def area(a, b, c):
    """
    Calculates the area of a triangle using Heron's formula.

    Args:
        a (float): The length of the first side of the triangle.
        b (float): The length of the second side of the triangle.
        c (float): The length of the third side of the triangle.

    Returns:
        float: The area of the triangle.
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle.

    Args:
        a (float): The length of the first side of the triangle.
        b (float): The length of the second side of the triangle.
        c (float): The length of the third side of the triangle.

    Returns:
        float: The perimeter of the triangle.
    """
    return a + b + c
