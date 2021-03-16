#!/usr/bin/env python3
""" async routine """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async routine """
    func = [wait_random(max_delay) for i in range(n)]
    x = []
    for j in asyncio.as_completed(func):
        r = await j
        x.append(r)
    return x
