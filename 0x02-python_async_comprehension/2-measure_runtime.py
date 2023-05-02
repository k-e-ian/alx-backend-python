#!/usr/bin/env python3.8
'''
File: 2-measure_runtime.py
'''

import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measure the total runtime of async_comprehension()
    '''
    start_time = perf_counter()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = perf_counter()

    return end_time - start_time
