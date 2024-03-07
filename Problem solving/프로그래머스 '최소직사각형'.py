'''
프로그래머스 - 최소직사각형

# 문제 설명
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 
이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.
아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

명함번호  가로  세로
  1	      60	50
  2	      30	70
  3	      60	30
  4	      80	40
  
가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 
하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 이때의 지갑 크기는 4000(=80 x 50)입니다.
모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.


# 제한 사항
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.


# 입출력 예
sizes                                                       result
[[60, 50], [30, 70], [60, 30], [80, 40]]	                4000
[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	            120
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	            133
'''




# 내 풀이
def solution(sizes):
    max_len = 0    # 가로 최대 길이
    max_len2 = 0   # 세로 최대 길이
    for idx, (x, y) in enumerate(sizes):
        if x < y:    # 가장 긴 변이 먼저 오도록 재정의
            sizes[idx][0], sizes[idx][1] = sizes[idx][1], sizes[idx][0]
        if sizes[idx][0] > max_len:    # 가로 최대길이
            max_len = sizes[idx][0]
        if sizes[idx][1] > max_len2:    # 세로 최대길이
            max_len2 = sizes[idx][1]
    return max_len * max_len2


# 다른 풀이
def solution(sizes):
    # 각 명함을 가로가 세로보다 길도록 재정의
    normalized_sizes = [sorted(size, reverse=True) for size in sizes]
    # 가장 긴 가로와 세로 길이 찾기
    max_width = max(size[0] for size in normalized_sizes)   # 제너레이터 표현식
    max_height = max(size[1] for size in normalized_sizes)
    # 지갑의 크기 계산
    return max_width * max_height