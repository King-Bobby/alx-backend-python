#!/usr/bin/env python3
"""
Contains the function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier
    """
    def multiplier_function(x: float) -> float:
        """multiplies a float by multiplier"""
        return x * multiplier
    return multiplier_function
