#!/usr/bin/env python3
"""
This module 1-async_comprehension.py, contains the function
async_comprehension()
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers
    using an async comprehension over async_generator.
    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()][:10]
