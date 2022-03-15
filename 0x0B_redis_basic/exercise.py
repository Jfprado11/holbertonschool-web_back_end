#!/usr/bin/env python3
"""Creating a class for using with redis
"""

from typing import Callable, Union
from functools import wraps
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """decorator to see how many times it was called
    """
    key_name = method.__qualname__

    @wraps(method)
    def calls_made(self, data):
        """count the times the method was called
        """
        stored = self._redis.get(key_name)
        if stored is None:
            self._redis.set(key_name, 1)
        else:
            self._redis.incr(key_name)
        return method(self, data)
    return calls_made


class Cache():
    """a class for the cache using the redis tool
    """

    def __init__(self) -> None:
        """iniatilizing the method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores the data into the redis application
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """getting the redis value
        """
        value = self._redis.get(key)

        if fn is not None:
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """ getting a string unicoded
        """
        return str(data.decode("utf-8"))

    def get_int(self, data: bytes) -> int:
        """getting the int values
        """
        return int(data.decode("utf-8"))
