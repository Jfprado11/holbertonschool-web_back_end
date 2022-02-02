#!/usr/bin/env python3
"""Learing the syntax of Asyncio"""

import asyncio
import random


async def wait_random(max_delay=10):
    """awaits for the delay"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
