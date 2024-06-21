'''
프로그래머스 - 타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165


# 문제 설명
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.


# 제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.


# 입출력 예
numbers	                target	    return
[1, 1, 1, 1, 1]	        3	        5
[4, 1, 2, 1]	        4	        2


'''


def solution(numbers, target):
    stack = [(0, 0)]  # 초기 상태, (현재 합계, 인덱스)
    count = 0

    while stack:
        current_sum, index = stack.pop()  # 스택에서 하나의 상태를 가져옴

        if index == len(numbers):  # 모든 숫자를 사용했을 때
            if current_sum == target:  # 현재 합이 타겟과 같으면 카운트 증가
                count += 1
        else:
            # 현재 숫자를 더하거나 빼는 두 가지 상태를 스택에 추가
            stack.append((current_sum + numbers[index], index + 1))
            stack.append((current_sum - numbers[index], index + 1))

    return count
