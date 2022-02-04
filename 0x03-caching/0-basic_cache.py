#!/usr/bin/python3
"""
Craetes a new class for a basic diccionary
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """a class to represent a cache"""

    def __init__(self) -> None:
        """iniatiliaze the class"""
        super().__init__()

    def put(self, key, item):
        """declares data to the cache"""
        if (key != None) and (item != None):
            self.cache_data[key] = item

    def get(self, key):
        """get the data looking for"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
