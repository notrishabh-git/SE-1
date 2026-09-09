"""Unit tests for Calculator module."""

import pytest
from src.calculator import Calculator


def test_add():
    """Test addition operation."""
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(2.5, 3.5) == 6.0


def test_subtract():
    """Test subtraction operation."""
    assert Calculator.subtract(10, 4) == 6
    assert Calculator.subtract(0, 5) == -5


def test_multiply():
    """Test multiplication operation."""
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(0, 100) == 0


def test_divide():
    """Test division operation and division by zero."""
    assert Calculator.divide(10, 2) == 5.0
    assert Calculator.divide(7, 2) == 3.5
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        Calculator.divide(10, 0)


def test_power():
    """Test exponentiation operation."""
    assert Calculator.power(2, 3) == 8
    assert Calculator.power(5, 0) == 1
