# from Terminal > pip install pytest
# from Terminal > pytest .
import calculator
import pytest

def test_calculator_add_small():
    # Arrange
    x: int = 1
    y: int = 2
    expected: int = 3

    # Activate
    actual: int = calculator.add(x, y)

    # Assert
    assert actual == expected

def test_calculator_sub_small():
    # Arrange
    x: int = 3
    y: int = 2
    expected: int = 1

    # Activate
    actual: int = calculator.subtract(x, y)

    # Assert
    assert actual == expected


def test_calculator_mul_small():
    # Arrange
    x: int = 1
    y: int = 2
    expected: int = 2

    # Activate
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected


def test_calculator_div_small():
    # Arrange
    x: int = 8
    y: int = 2
    expected: int = 4

    # Activate
    actual: int = calculator.divide(x, y)

    # Assert
    assert actual == expected

def test_calculator_power_small():
    # Arrange
    x: int = 9
    y: int = 0
    expected: int = 1

    # Activate
    actual: int = calculator.power(x, y)

    # Assert
    assert actual == expected


def test_calculator_sqrt_small():
    # Arrange
    x: int = 25
    expected: int = 5

    # Activate
    actual: int = calculator.sqrt(x)

    # Assert
    assert actual == expected


def test_calculator_prime_small():
    # Arrange
    x: int = 0
    expected: bool = False

    # Activate
    actual: int = calculator.is_prime(x)

    # Assert
    assert actual == expected


def test_calculator_factorial_small():
    # Arrange
    x: int = 5
    expected: int = 120

    # Activate
    actual: int = calculator.factorial(x)

    # Assert
    assert actual == expected


def test_calculator_div_zero_error_phase2():
    x: int = -3
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = calculator.factorial(x)

    assert str(ex.value) == "Cannot use numbers smaller then 0!"