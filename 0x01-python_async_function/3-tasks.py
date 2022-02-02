#!/usr/bin/env python3
"""a module of async """

import asyncio
from typing import TypeVar


wait_random = __import__('0-basic_async_syntax').wait_random

f = TypeVar("f", asyncio.Task)


def task_wait_random(max_delay: int) -> f:
    return asyncio.create_task(wait_random(max_delay))
