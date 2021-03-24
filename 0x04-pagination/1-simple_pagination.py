#!/usr/bin/env python3
""" Simple pagination function """
from typing import List


class Server:
    """ Simple pagination function """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ init """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page """
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)
        range = index_range(page, page_size)
        self.dataset()
        return self.__dataset[range[0]:range[1]]


def index_range(page, page_size):
    """ index range"""
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
