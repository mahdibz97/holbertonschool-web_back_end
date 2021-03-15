#!/usr/bin/env python3
""" tupl args """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ tupl args """
    return (k, v ** 2)
