#!/usr/bin/env python3
"""This module contains code for task
1 of python async comprehensions
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return
    the 10 random numbers.
    """

    return [i async for i in async_generator()]
