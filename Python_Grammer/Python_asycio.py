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




asyncio.run(main()) 코드는 파이썬의 비동기 프로그래밍에서 이벤트 루프(event loop)를 시작하고 관리하는 방법 중 하나입니다. asyncio 모듈을 사용하여 비동기 프로그래밍을 할 때, 비동기 함수(async def로 정의된)들을 실행하기 위해 이벤트 루프가 필요합니다.

asyncio.run() 함수는 다음과 같은 기능을 수행합니다:

이벤트 루프 생성: 새로운 이벤트 루프를 만들어서 실행합니다. 이미 실행 중인 이벤트 루프가 없을 경우에 사용됩니다.
코루틴 실행: 전달된 코루틴(main() 함수)을 이벤트 루프에서 실행하고, 코루틴이 완료될 때까지 기다립니다.
이벤트 루프 종료: 코루틴이 완료되면 이벤트 루프를 종료하고 자원을 정리합니다.
간단히 말해, asyncio.run(main())은 main() 함수 안에서 정의된 모든 비동기 작업이 시작되고 완료될 때까지 이벤트 루프를 실행하고 관리하는 역할을 합니다. 이렇게 함으로써 비동기 코드의 실행을 간편하게 처리할 수 있습니다.

# 이벤트 루프 실행
asyncio.run(main())

