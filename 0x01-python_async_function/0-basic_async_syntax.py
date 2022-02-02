#!/usr/bin/env bash
"""Learing the syntax of Asyncio"""

import asyncio
import random


async def wait_random(max_delay=10):
    i = random.uniform(0, max_delay)
    return i
