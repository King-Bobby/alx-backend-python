#!/usr/bin/env python3
"""
Contains the function safe_first_element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
