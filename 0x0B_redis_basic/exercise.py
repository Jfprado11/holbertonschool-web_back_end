#!/usr/bin/env python3
"""Creating a class for using with redis
"""

from typing import Callable, Union
import uuid
import redis


class Cache():
    """a class for the cache using the redis tool
    """

    def __init__(self) -> None:
        """iniatilizing the method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
