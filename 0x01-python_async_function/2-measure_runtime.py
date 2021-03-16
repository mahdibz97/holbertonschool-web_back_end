#!/usr/bin/env python3
""" measure an approximate elapsed time """
import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure an approximate elapsed time """
    t = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e = time.perf_counter() - t
    return e
