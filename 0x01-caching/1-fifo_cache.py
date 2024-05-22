#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    You must use self.cache_data - dictionary from
    the parent class BaseCaching
    """

    def __init__(self):
        """
        You can overload def __init__(self): but don’t forget
        to call the parent init: super().__init__()
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and
        following by a new line
        """
        if key is not None or item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
