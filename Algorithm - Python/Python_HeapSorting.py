import heapq

data = [10, 1, 5, 3, 4]
heapq.heapify(data)  # 리스트를 힙으로 변환

# 여러 요소를 힙에 추가
heapq.heappush(heap, 10)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)

print(heapq.heappop(heap))  # 출력: 1
