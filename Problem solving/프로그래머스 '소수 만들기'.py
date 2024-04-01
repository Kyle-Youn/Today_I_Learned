'''
프로그래머스 '소수만들기'
https://school.programmers.co.kr/learn/courses/30/lessons/12977

# 문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.


# 제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.


# 입출력 예
nums	        result
[1,2,3,4]	       1
[1,2,7,6,4]	       4
'''


import itertools

def solution(nums):
    answer = 0
    sum_list = list()

    # 조합 만들고 세트에 추가
    comb_iter = itertools.combinations(nums, 3)
    for comb in comb_iter:
        sum_list.append(sum(comb))
        
    # 3000까지의 소수를 모두 구해서 집합에 넣어 놓기
    prime_num = set(range(2, 3000 + 1))
    for i in range(2, 3000 +1):
        if i in prime_num:
            prime_num -= set(range(2*i, 3000 + 1, i))
    
    # 모든 조합의 합을 각각 소수인지 검사
    for num_sum in sum_list:
        if num_sum % 2 == 0:
            continue
        else:
            if num_sum in prime_num:
                answer += 1
    
    return answer

solution([1,2,7,6,4])