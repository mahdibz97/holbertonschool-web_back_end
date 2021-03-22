#!/usr/bin/python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic dictionary """
    def put(self, key, item):
        """ assign to the dictionary self.cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
