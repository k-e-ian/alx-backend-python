#!/usr/bin/env python3.8
'''
File: 0-async_generator.py
'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous generator that yields a random number between 0 and 10, 10 times."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
