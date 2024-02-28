# 다익스트라 구현(heapq 라이브러리)
import heapq

def dijkstra(graph, start, final):
    costs = {}
    priority_q = []
    heapq.heappush(priority_q, (0,start))
    
    while priority_q:
        cur_cost, cur_v = heapq.heappop(priority_q)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(priority_q, (next_cost, next_v))
    return costs[final]


# 그래프(방향그래프, 인접리스트 형태)
graph = {
    1: [2, 4],
    2: [3, 5, 6],
    3: [6],
    4: [3, 7],
    5: [8],
    6: [5],
    7: [6, 8],
    8: []
}

# 다익스트라 함수 호출
dijkstra(graph, 1, 8)
   