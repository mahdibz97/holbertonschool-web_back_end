#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """ Simple helper function """
    f = (page - 1) * page_size
    return (f, f + page_size)
