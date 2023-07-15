#!/usr/bin/env python3

"""This module contains code for task
4 of python async funtions
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes an integer max_delay and
    returns a asyncio.Task.
    """

    delays = []
    routines = []

    for i in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: delays.append(x.result()))
        routines.append(task)

    await asyncio.gather(*routines)

    return delays
