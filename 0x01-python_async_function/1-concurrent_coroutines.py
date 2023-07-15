#!/usr/bin/env python3

"""This module contains code for task
1 of python async funtions
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay) -> float:
    """Takes in 2 args n and max_delay and spawns
    wait_random n times with the specified max_delay.
    """
    delays = []
    routines = []

    for _ in range(n):
        b = asyncio.create_task(wait_random(max_delay))
        b.add_done_callback(lambda x: delays.append(x.result()))
        routines.append(b)

    await asyncio.gather(*routines)

    return delays
