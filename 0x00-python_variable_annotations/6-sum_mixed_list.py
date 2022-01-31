#!/usr/bin/env python3
"""sum of a mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of int and float of a list"""
    whole_sum: float = 0
    for item in mxd_lst:
        whole_sum += item
    return whole_sum
