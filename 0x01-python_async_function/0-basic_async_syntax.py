#!/usr/bin/env python3
""" asynchronous coroutine """
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
