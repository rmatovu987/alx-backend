#!/usr/bin/env python3
"""Create a class LIFOCache that
inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def __init__(self) -> None:
        """ initialize of class """
        self.temp_list = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            self.temp_list.append(key)
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = self.temp_list.pop(0)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")

    def get(self, key):
        """ Get an item by key
        """
        if (key is None) or not (key in self.cache_data):
            return None
        self.temp_list.insert(len(self.temp_list),
                              self.temp_list.pop(self.temp_list.index(key)))
        return self.cache_data.get(key)
