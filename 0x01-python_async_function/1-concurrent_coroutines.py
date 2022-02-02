#!/usr/bin/env python3
"""a module of async """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a numbers"""
    list_of_data = []
    for i in range(n):
        list_of_data.append(asyncio.create_task(wait_random(max_delay)))
    resulrs = await asyncio.gather(*list_of_data)
    return sorted(resulrs)
