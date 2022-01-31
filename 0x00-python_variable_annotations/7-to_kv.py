#!/usr/bin/env python3
"""string to tuple"""

import math
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple witha string and float"""
    num: float = float(v ** 2)
    return (k, num)
