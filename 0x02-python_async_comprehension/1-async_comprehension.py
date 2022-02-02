#!/usr/bin/env python3
"""Creating a async comprehision"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """cretes the numbers in generator"""
    numbers = [i async for i in async_generator()]
    return numbers
