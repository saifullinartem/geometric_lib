 Project Documentation

## Overview of the Solution
This project is designed to calculate the area and perimeter of basic geometric shapes, including circles, rectangles, and squares. The formulas used in this project are straightforward and allow users to easily compute the required values based on user-defined dimensions.

The primary purpose of this solution is to provide a clear and efficient way to perform geometric calculations, which can be useful in various applications such as architectural design, academic teaching, and computational geometry.

## Functions

### `calculate_area_circle(radius: float) -> float`
Calculates the area of a circle given its radius.

**Parameters**:
- `radius` (float): The radius of the circle.

**Returns**:
- (float): The area of the circle.

**Example**:
python
area = calculate_area_circle(5)
print(area) # Output: 78.53981633974483


### `calculate_area_rectangle(length: float, width: float) -> float`
Calculates the area of a rectangle given its length and width.

**Parameters**:
- `length` (float): The length of the rectangle.
- `width` (float): The width of the rectangle.

**Returns**:
- (float): The area of the rectangle.

**Example**:
python
area = calculate_area_rectangle(4, 6)
print(area) # Output: 24.0


### `calculate_area_square(side: float) -> float`
Calculates the area of a square given its side length.

**Parameters**:
- `side` (float): The length of the side of the square.

**Returns**:
- (float): The area of the square.

**Example**:
python
area = calculate_area_square(3)
print(area) # Output: 9.0


### `calculate_perimeter_circle(radius: float) -> float`
Calculates the perimeter (circumference) of a circle given its radius.

**Parameters**:
- `radius` (float): The radius of the circle.

**Returns**:
- (float): The perimeter of the circle.

**Example**:
python
perimeter = calculate_perimeter_circle(5)
print(perimeter) # Output: 31.41592653589793


### `calculate_perimeter_rectangle(length: float, width: float) -> float`
Calculates the perimeter of a rectangle given its length and width.

**Parameters**:
- `length` (float): The length of the rectangle.
- `width` (float): The width of the rectangle.

**Returns**:
- (float): The perimeter of the rectangle.

**Example**:
python
perimeter = calculate_perimeter_rectangle(4, 6)
print(perimeter) # Output: 20.0


### `calculate_perimeter_square(side: float) -> float`
Calculates the perimeter of a square given its side length.

**Parameters**:
- `side` (float): The length of the side of the square.

**Returns**:
- (float): The perimeter of the square.

**Example**:

