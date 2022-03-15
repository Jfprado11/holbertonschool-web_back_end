#!/usr/bin/env python3
"""Creating a class for using with redis
"""

from typing import Union
import uuid
import redis


class Cache():
    """a class for the cache using the redis tool
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data) -> str:
        """stores the data into the redis application
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
