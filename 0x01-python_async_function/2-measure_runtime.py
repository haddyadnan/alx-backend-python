#!/usr/bin/env python3
"""
measure run time
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: float) -> float:
    """
    measure time
    """
    t_start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t_end = time.perf_counter() - t_start
    return t_end / n
