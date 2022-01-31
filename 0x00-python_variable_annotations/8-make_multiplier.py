#!/usr/bin/env python3
"""returns a function that multiplies a float by multiplier."""

from typing import Callable


def multiply(x) -> float:
    """multiplies a number"""
    return x * x


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    return multiply
