#!/usr/bin/env python3
"""
Implementing the FIFO caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Class to represent a fifo cache"""

    def __init__(self) -> None:
        """Initialiaze the class"""
        super().__init__()

    def put(self, key, item):
        """store data in the dict cache"""
        if (key is not None) and (item is not None):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                keys = next(iter(self.cache_data))
                del self.cache_data[keys[0]]
                print("DISCARD: {}".format(keys[0]))

    def get(self, key):
        """get the data looking for"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
