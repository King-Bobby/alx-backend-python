#!/usr/bin/env python3
"""
Contains the function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int or float v, returns a tuple (k, v^2)."""
    return (k, float(v)**2)
