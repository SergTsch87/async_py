#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio


# async def f():
#     await asyncio.sleep(1)
#     return "Hello, World!"


# async def g():
#     result = await f()
#     return result

# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#     await asyncio.sleep(1)


async def f(x):
    y = await z(x)  # Okay - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # Okay - this is an async generator

# async def m(x):
#     yield from gen(x)  # No - SyntaxError

# def n(x):
#     y = await z(x)  # No - SyntaxError (no `async def` here)
#     return y


async def main():
    # await asyncio.gather(count(), count(), count())
    await g()


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in: {elapsed:0.2f} seconds")