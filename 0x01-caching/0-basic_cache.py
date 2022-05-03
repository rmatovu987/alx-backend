#!/usr/bin/env python3
"""
Create a class BasicCache that
inherits from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def put(self, key, item):
        """Assign the dictionary"""
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """Get item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
