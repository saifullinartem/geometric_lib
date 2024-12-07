
import pytest
from calculate import Calculator

def test_calculator_add():
    calculator = Calculator()
    a = 2
    b = 3
    expected = 5

    result = calculator.add(a, b)

    
    assert result == expected, f"Expected {expected}, got {result}"

def test_calculator_subtract():
    calculator = Calculator()
    a = 5
    b = 3
    expected = 2

    result = calculator.subtract(a, b)

    assert result == expected, f"Expected {expected}, got {result}"

def test_calculator_multiply():
    calculator = Calculator()
    a = 4
    b = 3
    expected = 12

    result = calculator.multiply(a, b)

    assert result == expected, f"Expected {expected}, got {result}"

def test_calculator_divide():
    calculator = Calculator()
    a = 10
    b = 2
    expected = 5

    result = calculator.divide(a, b)

    assert result == expected, f"Expected {expected}, got {result}"

def test_calculator_divide_by_zero():
    calculator = Calculator()
    a = 10
    b = 0

    with pytest.raises(ValueError):
        calculator.divide(a, b)

def test_calculator_invalid_input():
    calculator = Calculator()

    with pytest.raises(TypeError):
        calculator.add("two", 3)

    with pytest.raises(TypeError):
        calculator.subtract(5, None)

    with pytest.raises(TypeError):
        calculator.multiply(4, "three")

    with pytest.raises(TypeError):
        calculator.divide("ten", 2)
