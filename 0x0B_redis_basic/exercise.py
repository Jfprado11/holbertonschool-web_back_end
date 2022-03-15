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
        _redis = redis.Redis()
        _redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores the data into the redis application
        """
        key = str(uuid.uuid4())
        redis.Redis().set(key, data)
        return key
