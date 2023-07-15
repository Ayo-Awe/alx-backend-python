#!/usr/bin/env python3

"""This module contains code for task
1 of python async funtions
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
        and returns total_time / n.
        """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter()-start

    return total/n
