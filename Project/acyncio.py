import acyncio

async def tast(name):
  await asyncio.sleep(1)
  print(f"{name} 끝!"

async def main():
  await asyncio.gather(tast("A"), tast("B"))

asyncio.run(main())
