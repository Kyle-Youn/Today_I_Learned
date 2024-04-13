'''
프로그래머스 - '완주하지 못한 선수'
https://school.programmers.co.kr/learn/courses/30/lessons/42576


# 문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


# 제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.


# 입출력 예
participant	completion	                                                                                return
["leo", "kiki", "eden"]	["eden", "kiki"]	                                                            "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	        "vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	                                    "mislav"
'''


# 시간복잡도 O(n)
def solution(participant, completion):
    particip_dict = {}    # (참가자 - 완주자) 연산을 위한 딕셔너리 생성. 동명이인이 가능하므로
    answer = ''
    
    for particip in participant:    # 참가자의 이름을 KEY, 동명이인 포함 완주자의 숫자 Value로 하여 딕셔너리에 카운트 
        if particip not in particip_dict:
            particip_dict[particip] = 1
        else:
            particip_dict[particip] += 1
            
    for complet in completion:    # 완주자 수만큼 빼기 연산
        particip_dict[complet] -= 1
    
    find_uncompletion = list(particip_dict.items())
    
    for x in uncompletion:    # 완주하지 못한 1인 찾기
        if x[1] == 1:
            answer = x[0]
    
    return answer