#!/usr/bin/env python3
""" returns a asyncio.Task """
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a asyncio.Task """
    func = [task_wait_random(max_delay) for i in range(n)]
    x = []
    for j in asyncio.as_completed(func):
        r = await j
        x.append(r)
    return x
