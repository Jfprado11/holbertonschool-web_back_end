#!/usr/bin/env python3
"""Cratinag a async generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """creates an array and yields it"""
    for i in range(10):
        random_number = random.uniform(0, 10)
        yield random_number
        await asyncio.sleep(1)
