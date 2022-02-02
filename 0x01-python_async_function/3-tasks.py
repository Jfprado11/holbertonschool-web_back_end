#!/usr/bin/env python3
"""a module of async """

import asyncio
from typing import NewType


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creating a task_delay"""
    return asyncio.create_task(wait_random(max_delay))
