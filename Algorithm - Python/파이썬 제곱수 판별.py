# Python에서 특정 자연수가 어떤 정수를 제곱한 수인지 판별하는 코드

if int(k ** 0.5) ** 2 == k:
    print(True)
else:
    print(False)
# k = 25일 때, True
# k = 26일 때, False