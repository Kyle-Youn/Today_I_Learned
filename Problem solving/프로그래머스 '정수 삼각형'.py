'''
프로그래머스 '정수 삼각형'
https://school.programmers.co.kr/learn/courses/30/lessons/43105


# 문제 설명
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

# 제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

# 입출력 예
triangle	result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30
'''


# 시간복잡도 O(n**2)
def solution(triangle):
    for i in range(len(triangle)):
        if i == 0:
            continue
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                if triangle[i-1][j-1] >=  triangle[i-1][j]:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
    return max(triangle[len(triangle)-1])


'''
탑다운 방식으로 특정 노드까지 도달하는 모든 경우의 수에서 최대값을 가지는 하나의 경로만 그 노드에 저장하면서 진행하는 풀이.
이전 단계에서 출발하여 다음 단계 특정 노드에 도달하는 경우의 수는 2가지만 존재하는 것에 주목할 필요가 있다.
그 두 가지 경우의 수 중에서 더 큰 값만 노드에 저장
'''