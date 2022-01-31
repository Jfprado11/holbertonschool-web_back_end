#!/usr/bin/env python3
"""return the sum of whole list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the summ of all elements in a list"""
    whole_sum: float = 0
    for item in input_list:
        whole_sum += item
    return whole_sum
