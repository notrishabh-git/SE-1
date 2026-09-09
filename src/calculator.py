"""Calculator module providing basic arithmetic and statistical operations."""

from typing import Union

Number = Union[int, float]


class Calculator:
    """A standard arithmetic calculator with error handling."""

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """Return the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a: Number, b: Number) -> float:
        """Return the quotient of two numbers.

        Raises:
            ValueError: If denominator is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def power(base: Number, exponent: Number) -> Number:
        """Return base raised to power exponent."""
        return base**exponent
