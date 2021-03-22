#!/usr/bin/python3
""" LIFO Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """

    def __init__(self):
        """ init """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ assign to the dictionary self.cache_data """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.order[-1]]
                    print("DISCARD:", self.order[-1])
                    self.order.pop(-1)
                self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
