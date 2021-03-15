#!/usr/bin/env python3
""" multi args """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multi args """
    def func(i):
        return i * multiplier
    return func
