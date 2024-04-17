'''
프로그래머스 '더 맵게'
https://school.programmers.co.kr/learn/courses/30/lessons/42626


# 문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.


# 제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.


# 입출력 예
scoville	                K	    return
[1, 2, 3, 9, 10, 12]	    7	      2
'''


# 시간복잡도 O(nlogn)
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)    # scoville을 heapify
    
    while scoville[0] < K:
        if len(scoville) < 2:    # K 이상으로 도달하지 못한 상황에서, 음식이 2개 미만일 경우 -1 반환
            return -1
        food1 = heapq.heappop(scoville)    # 가장 맵지 않은 음식 pop
        food2 = heapq.heappop(scoville)    # 두 번째로 가장 맵지 않은 음식 pop
        mix_food = food1 + food2 * 2    # 음식 합치기
        heapq.heappush(scoville, mix_food)    # 합친 음식을 heap에 다시 push
        answer += 1    # 섞은 횟수 1추가
        
    return answer