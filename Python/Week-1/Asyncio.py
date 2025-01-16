#Asynchronus Programming is NOT multithreading , is NOT multi processing 
#It is concurrent programming 

import asyncio

async def main():

    task = asyncio.create_task(other_function())
    print("A")
    print("B")
    await task
async def other_function():
    print("1")
    await asyncio.sleep(5)
    print("2")

asyncio.run(main())