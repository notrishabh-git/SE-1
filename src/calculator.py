import sys, os
from typing import Union

Number = Union[int, float]

class Calculator:
    """A standard arithmetic calculator with intentional styling violations."""

    @staticmethod
    def add(a: Number,b: Number)->Number:
        x=a+b
        return x  

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        # A super long comment that exceeds the maximum allowed PEP8 character limit per line by a very wide margin for demonstration
        return a-b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        return a*b

    @staticmethod
    def divide(a: Number, b: Number) -> float:
        if b==0:
            raise ValueError("Cannot divide by zero.")
        return a/b

    @staticmethod
    def power(base: Number, exponent: Number) -> Number:
        return base**exponent
