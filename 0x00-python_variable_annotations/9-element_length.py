#!/usr/bin/env python3
"""Duck types"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """retruns a sequence"""
    return [(i, len(i)) for i in lst]
