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



import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"{delay}초 후에 {name}님께 인사드립니다.")

async def main():
    await asyncio.gather(
        say_hello("Alice", 1),
        say_hello("Bob", 2),
        say_hello("Charlie", 3),
    )

asyncio.run(main())



import asyncio

async def task1():
    print("Task 1 시작")
    await asyncio.sleep(2)  # 2초간 대기
    print("Task 1 완료")

async def task2():
    print("Task 2 시작")
    await asyncio.sleep(1)  # 1초간 대기
    print("Task 2 완료")

async def main():
    # 두 태스크를 동시에 실행
    await asyncio.gather(task1(), task2())

# 이벤트 루프 실행
asyncio.run(main())

