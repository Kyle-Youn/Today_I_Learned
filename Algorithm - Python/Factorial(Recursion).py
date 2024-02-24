# 팩토리얼 구현(재귀함수)
def factorial(n):
    if n < 0:   # 자연수 입력이 아닐 시
        return 'Only input natural number'
    
    if n == 0 or n == 1:    #base case
        return 1
    else:
        return n * factorial(n - 1)