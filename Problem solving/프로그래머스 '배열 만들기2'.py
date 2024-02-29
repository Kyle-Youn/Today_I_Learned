'''
# 프로그래머스 '배열 만들기2'
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

입출력 예
l= 5, r= 555, result= [5, 50, 55, 500, 505, 550, 555]
l= 10, r= 20, result= [-1]
'''

def solution(l, r):
    answer = []
    for num in range(l, r+1):
        if all(ch in '05' for ch in str(num)):
            answer.append(num)
    return answer if answer else [-1]