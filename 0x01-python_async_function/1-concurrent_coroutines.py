#!/usr/bin/env python3
"""Module for task 1
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> float:
    """
    async routine called wait_n that takes in 2
    int arguments (in this order): n and max_delay
    """
    my_list = []
    for i in range(n):
        my_list.append(wait_random(max_delay))
    
    delays = await asyncio.gather(*tasks)

    sorted_delays = []

    for delay in delays:
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                break
        else:
            sorted_delays.append(delay)
    
    return sorted_delays