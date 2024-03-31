'''
프로그래머스 '소수찾기'
https://school.programmers.co.kr/learn/courses/30/lessons/12921


# 문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)


# 제한 조건
n은 2이상 1000000이하의 자연수입니다.


# 입출력 예
n	    result
10	      4
5	      3
'''

# 에라토스테네스의 체. 시간복잡도 O(nloglogn)
def solution(n):
    primes = set(range(2, n+1))    # 세트 자료형에 2부터 n까지 모든 자연수 생성
    
    for num in range(2, n+1):
        if num in primes:
            primes -= set(range(num*2, n+1, num))    # num 자체를 제외한 모든 배수를 prime 세트와 차집합 연산
    return len(primes)