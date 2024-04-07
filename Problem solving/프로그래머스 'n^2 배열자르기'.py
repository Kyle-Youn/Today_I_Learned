'''
프로그래머스 'n ** 2' 배열 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/87390


# 문제 설명
정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.


제한사항
1 ≤ n ≤ 107
0 ≤ left ≤ right < n2
right - left < 105


n	    left	right	   result
3	     2	      5	       [3,2,2,3]
4	     7	      14       [4,3,3,3,4,4,4,4]
'''


# 시간복잡도 O(n)
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):    # left 인덱스부터 right인덱스까지
        tmp = (i % n) + 1    # 인덱스와 규칙성을 기반으로 평탄화한 배열의 특정 인덱스 값을 할당
        if (i // n) - (i % n) > 0:    # 인덱스를 n으로 나눈 (몫 - 나머지)가 0보다 크면 tmp에 해당 값을 추가로 더해서 할당한다.
            tmp += (i // n) - (i % n)
        answer.append(tmp)
    return answer