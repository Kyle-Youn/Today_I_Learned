'''
프로그래머스 '행렬의 곱셈'
https://school.programmers.co.kr/learn/courses/30/lessons/12949


# 문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.


# 입출력 예
arr1	                                                    arr2	                                                    return
[[1, 4], [3, 2], [4, 1]]	                                [[3, 3], [3, 3]]	                                        [[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	                        [[5, 4, 3], [2, 4, 1], [3, 1, 1]]	                        [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''


# 시간복잡도 (n**3)
def solution(arr1, arr2):
    # 결과 행렬의 크기를 결정합니다. arr1의 행의 수와 arr2의 열의 수입니다.
    result = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    # arr1의 각 행에 대해 반복합니다.
    for i in range(len(arr1)):
        # arr2의 각 열에 대해 반복합니다.
        for j in range(len(arr2[0])):
            # arr1의 i번째 행과 arr2의 j번째 열을 곱셈합니다.
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
                
    return result