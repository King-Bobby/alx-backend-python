#!/usr/bin/env python3
"""
Contains the function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """takes a list of floats and ints and returns the sum"""
    total = 0.0
    for num in mxd_list:
        total += num
    return total
