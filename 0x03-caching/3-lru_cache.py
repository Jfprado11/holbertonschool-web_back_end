#!/usr/bin/env python3
"""
Implementing the LRU  caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Class to represent a LRU cache"""

    def __init__(self) -> None:
        """Initialiaze the class"""
        super().__init__()

    def put(self, key, item):
        """store data in the dict cache"""
        if (key is not None) and (item is not None):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                last_item = list(self.cache_data)[-2]
                del self.cache_data[last_item]
                print("DISCARD: {}".format(last_item))

    def get(self, key):
        """get the data looking for"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
