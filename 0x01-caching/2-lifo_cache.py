#!/usr/bin/env python3
"""Create a class LIFOCache that
inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def put(self, key, item):
        """
        Assign to the dictionary
        :param key:
        :param item:
        :return:
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            temp = list(self.cache_data.keys())
            if len(temp) > self.MAX_ITEMS:
                self.cache_data.pop(temp[len(temp) - 1])
                print(f'DISCARD: {temp[len(temp) - 1]}')

    def get(self, key):
        """
        Get item by key
        :param key:
        :return:
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
