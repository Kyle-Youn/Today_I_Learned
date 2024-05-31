'''
파이썬 시간측정 코드
'''


# perf.counter() 함수는 코드의 연산시간 외에도 sleep, file io 등 pending에 들어가는 시간까지 모두 포함해서 측정
import time
start_time = time.perf_counter()
'''
시간 측정할 코드
'''
end_time = time.perf_counter()
print(f"{end_time - start_time}초")



# process_time() 함수는 코드의 순수 연산시간만을 측정. 예를들어, time.sleep(5) 코드를 삽입하더라도 이러한 pending 시간은 측정되지 않음.
import time
start_time = time.process_time()
'''
시간 측정할 코드
'''
time.sleep(5)
end_time = time.process_time()
print(f"{end_time - start_time}초")