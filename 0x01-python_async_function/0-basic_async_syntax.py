#!/usr/bin/env python3
"""0-basic_async_syntax module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for seconds"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
