# 시간복잡도 (n**3)
def solution(arr1, arr2):
    # 결과 행렬의 크기를 결정. arr1의 행의 수와 arr2의 열의 수
    result = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    # arr1의 각 행에 대해 반복
    for i in range(len(arr1)):
        # arr2의 각 열에 대해 반복
        for j in range(len(arr2[0])):
            # arr1의 i번째 행과 arr2의 j번째 열을 곱셈
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
                
    return result