#!/usr/bin/env python3
"""
Contains the function wait_random
"""


import asyncio
import random


async def wait_random(max_delay=10):
    """
    Takes in a value,
    then waits for a random delay between 0 and that value,
    then returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
