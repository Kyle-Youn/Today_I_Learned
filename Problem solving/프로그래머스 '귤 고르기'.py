'''
프로그래머스 - 귤고르기

경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 
그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 
경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 
귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
1 ≤ k ≤ tangerine의 길이 ≤ 100,000
1 ≤ tangerine의 원소 ≤ 10,000,00

# 입출력 예
k = 6, tangerine = [1, 3, 2, 5, 4, 5, 2, 3], result = 3
k = 4, tangerine = [1, 3, 2, 5, 4, 5, 2, 3], result = 2
k = 2, tangerrine = [1, 1, 1, 1, 2, 2, 2, 3], result = 1
'''




def solution(k, tangerine):
    # 귤 사이즈별 갯수 카운트 - 딕셔너리 이용
    tang_dict = {}
    for tang in tangerine:
        if tang not in tang_dict:
            tang_dict[tang] = 1
        else:
            tang_dict[tang] += 1
    
    # 귤 (사이즈, 갯수)를 담은 리스트를 갯수의 내림차순으로 정렬
    tang_list = sorted(list(tang_dict.items()), key = lambda x:x[1], reverse = True)
    
    # 한 박스 k개의 귤을 담기 위해서 몇 종류의 귤 사이즈가 들어가야하는지 최솟값을 카운트 후 리턴
    answer = 0
    sum_num = 0
    for _, num in tang_list:
        sum_num += num
        answer += 1
        if sum_num >= k:
            break
        if sum_num < k:
            continue
    return answer