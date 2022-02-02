#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the tiem it tooks to parrale all the values"""
    start = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(), async_comprehension(), async_comprehension())
    end = time()
    return end - start
