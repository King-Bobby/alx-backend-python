#!/usr/bin/env python3
"""
Conatins the function element_length
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list"""
    return [(i, len(i)) for i in lst]
