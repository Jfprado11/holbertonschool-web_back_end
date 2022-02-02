#!/usr/bin/env python3
"""a module of async """

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a numbers"""
    list_of_data = []
    for i in range(n):
        object_num = task_wait_random(max_delay)
        list_of_data.append(object_num)
    resulrs = await asyncio.gather(*list_of_data)
    return sorted(resulrs)
