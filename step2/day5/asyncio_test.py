import asyncio

async def task1():
    await asyncio.sleep(2)
    print('TASK1')
    return "task1"

async def task2():
    await asyncio.sleep(2)
    print('TASK2')
    return "task2"


async def main():
    result = await asyncio.gather(task1(), task2())
    print(result)

asyncio.run(main())



