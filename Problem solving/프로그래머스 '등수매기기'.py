'''
영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때,
영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
0 ≤ score[0], score[1] ≤ 100
1 ≤ score의 길이 ≤ 10
score의 원소 길이는 2입니다.
score는 중복된 원소를 갖지 않습니다.

# 입출력 예
score = [[80, 70], [90, 50], [40, 70], [50, 80]], 	result = [1, 2, 4, 3]
score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]], result = [4, 4, 6, 2, 2, 1, 7]
'''




# 내 풀이        # O(nlogn)
def solution(score):
    answer = [None for _ in range(len(score))]
    current_rank = 1
    ever_score = [(i, sum(sco)/2) for i,sco in enumerate(score)]
    ever_score.sort(key= lambda x:x[1], reverse= True)
    for i,(idx, sco) in enumerate(ever_score):
        if i > 0 and sco != ever_score[i-1][1]:
            current_rank = i + 1
        answer[idx] = current_rank
    return answer




# 다른 분 풀이        # O(n**2)
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]