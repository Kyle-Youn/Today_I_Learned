import sys

print("파이썬에 대해 알아봅시다")
orig_stdout = sys.stdout
file5 = open("c:\\temp\\test1.txt", "a")
sys.stdout = file5 # 표준출력을 모니터에서 file5로 변경

print("파이썬에 대해 알아봅시다")
file5 = close()

sys.stdout = orig_stdout # 표준출력을 원래대로 변경(모니터)
print("저장이 완료되었습니다")
