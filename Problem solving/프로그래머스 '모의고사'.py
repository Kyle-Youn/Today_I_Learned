'''
프로그래머스 '모의고사'
https://school.programmers.co.kr/learn/courses/30/lessons/42840


# 문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


# 제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.


# 입출력 예
answers	        return
[1,2,3,4,5]	    [1]
[1,3,2,4,2]	    [1,2,3]
'''


# 시간복잡도 O(n)
def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo1_num = 0
    supo2_num = 0
    supo3_num = 0
    
    supo1 = supo1 * (len(answers) // len(supo1)) + supo1[:len(answers) % len(supo1)]    # answers 리스트와 길이 일치시키기
    supo2 = supo2 * (len(answers) // len(supo2)) + supo2[:len(answers) % len(supo2)]
    supo3 = supo3 * (len(answers) // len(supo3)) + supo3[:len(answers) % len(supo3)]
    
    exam = zip(supo1, supo2, supo3, answers)    # 정답과 답안을 튜플로 묶기
    
    for ans1, ans2, ans3, ans in exam:    # 튜플을 순회하면서 정답일 경우 변수에 맞춘 문제수 추가
        if ans1 == ans:
            supo1_num += 1
        if ans2 == ans:
            supo2_num += 1
        if ans3 == ans:
            supo3_num += 1
    
    max_score = max([supo1_num, supo2_num, supo3_num])   # 최고 점수 찾기
            
    return sorted([idx+1 for idx, score in enumerate([supo1_num, supo2_num, supo3_num]) if score == max_score])    # 최고점수와 일치하는 점수만 찾아 index+1로 사람 번호 추가