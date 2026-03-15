#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio
import random


COLORS = (
    "\033[0m",   # End of color
    "\033[36m",   # Cyan
    "\033[91m",   # Red
    "\033[35m",   # Maagenta
)


async def makerandom(delay, threshold=6):
    color = COLORS[delay]
    print(f"{color}Initiated makerandom with delay: {delay}s")
    while (number := random.randint(0, 10)) <= threshold:
        print(f"{color}makerandom({delay}) == {number} too low; retrying.")
        await asyncio.sleep(delay)
    
    print(f"{color}---> Finished: makerandom({delay}) == {number}" + COLORS[0])
    return number


async def main():
    return await asyncio.gather(
        makerandom(1, 9),
        makerandom(2, 8),
        makerandom(3, 8),
    )


if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print(f"\nr1: {r1}\nr2: {r2}\nr3: {r3}")