import asyncio

async def count_down(name, seconds):
    print(f"{name} 카운트다운 시작")
    for i in range(seconds, 0, -1):
        print(f"{name}: {i}")
        await asyncio.sleep(1)  # 1초 대기
    print(f"{name} 카운트다운 완료!")

async def main():
    # 두 개의 카운트다운을 동시에 실행
    task1 = asyncio.create_task(count_down("타이머1", 3))
    task2 = asyncio.create_task(count_down("타이머2", 5))

    # 두 태스크가 모두 완료될 때까지 대기
    await task1
    await task2

asyncio.run(main())
