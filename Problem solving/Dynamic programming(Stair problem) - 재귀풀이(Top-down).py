# 다이내믹 프로그래밍 구현(계단 문제) - 재귀풀이(Top-down)

'''
계단을 올라가고 있다.
이 계단의 꼭대기에 도착하려면 n개의 steps만큼 올라가야 한다.
한 번 올라갈 때마다 1step 또는 2steps 올라갈 수 있다.
꼭대기에 도달하는 방법의 개수는 총 몇 가지 일까요?
'''

memoization = {}

def stair(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n not in memoization:
        memoization[n] = cs(n-1) + cs(n-2)
    return memoization[n]