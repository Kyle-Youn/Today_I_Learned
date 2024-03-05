'''
프로그래머스 - H-index

# 문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상일 때, h의 최댓값이 이 과학자의 H-Index입니다.
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.


# 제한 사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# 입출력 예
citations = [3, 0, 6, 1, 5], return = 3
'''




def solution(citations):
    citations.sort(reverse=True)
    H_Index = 0
    for i, cit in enumerate(citations):
        if i+1 <= cit:
            H_Index = i+1
        else:
            break
    return H_Index