#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio


async def f():
    await asyncio.sleep(1)
    return "Hello, World!"


async def g():
    result = await f()
    return result

# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#     await asyncio.sleep(1)


async def main():
    # await asyncio.gather(count(), count(), count())
    await g()


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in: {elapsed:0.2f} seconds")