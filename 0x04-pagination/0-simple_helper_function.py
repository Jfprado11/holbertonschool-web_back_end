#!/usr/bin/env python3
"""
Obtains the indexes for the pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple with indexes to a list of pagination"""
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return (start_idx, end_idx)
