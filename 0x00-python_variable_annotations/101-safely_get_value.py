#!/usr/bin/env python3
"""duck-typed annotations"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """returning a value"""
    if key in dct:
        return dct[key]
    else:
        return default
