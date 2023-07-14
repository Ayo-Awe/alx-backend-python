#!/usr/bin/env python3

"""This module contains code for task
0 of python async funtions
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """This async funtion waits for a random
    delay between 0 and 10 then returns it
    """

    return random.uniform(0, max_delay)
