#!/usr/bin/env python3
"""This module contains code for task
0 of python async comprehensions
"""

import random
import asyncio


async def async_generator() -> float:
    """Loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
