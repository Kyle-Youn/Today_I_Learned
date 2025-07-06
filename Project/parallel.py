import concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import math

def basic_example():
  """concurrent.futures 기본 사용법"""

  # I/O Bound 작업 예시 (ThreadPoolExcutor 적합)
  def simulate_io_task(n):
    """I/O 작업 시뮬레이션"""
    time.sleep(0.1)    # I/O 대기 시뮬레이션
    return n*n
  
  # CPU Bound 작업 예시 (ProcessPoolExcutor 적합)
  def cpu_intensive_task(n):
    """CPU 집약적 작업"""
    result = 0
    for i in range(n * 100000):    # 실제 CPU 연산
     result += math.sqrt(i + 1)
    return result

  numbers = [1, 2, 3, 4, 5]

  print("I/O Bound 작업 (ThreadPoolExecutor):")
  with ThreadPoolExecutor(max_workers=5) as executor:
    io_results = list(executor.map(simulate_io_task, numbers))
  print(f"결과: {io_results}")

  print("\nCPU Bound 작업 (ProcessPoolExecutor):")
  with ProcessPoolExecutor(max_workers=5) as executor:
    cpu_results = list(executor.map(cpu_intensive_task, numbers))
    print(f"결과: {cpu_results[:3]}...")  # 일부만 출력
