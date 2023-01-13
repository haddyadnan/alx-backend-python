#!/usr/bin/env python3
"""
async execute multiple coroutines
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return float
    """

    delay = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))

    return sorted(delay)
