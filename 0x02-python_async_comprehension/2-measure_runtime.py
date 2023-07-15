#!/usr/bin/env python3
"""This module contains code for task
2 of python async comprehensions
"""

import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times
    in parallel using asyncio.gather
    """
    start = perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    return perf_counter() - start
