from concorrent.futures import ThreadPoolExecutor

# 함수 정의
def some_task(arguments):
  # Do something
  return "Result"

# ThreadPoolExecutor를 사용한 병렬 실행
with ThreadPoolExecutor(max_workers=10) as executor:
  # 함수를 10개의 쓰레드에서 실행
  futures = [executor.submit(some, task, args) for args in range(10)]

  # 결과 출력
  for future in futures:
    print(future.result())
