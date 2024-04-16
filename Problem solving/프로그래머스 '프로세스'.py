from collections import deque

def solution(priorities, location):
    answer = 0
    max_prior = max(priorities)
    priorities = [(i, q) for i, q in enumerate(priorities)]
    prior_deque = deque(priorities)
    
    while prior_deque:
        if prior_deque[0][1] >= max_prior:
            i, q = prior_deque.popleft()
            answer += 1
            if q == max_prior:
                max_prior = max(prior_deque)
            if i == location:
                break
        else:
            prior_deque.append(prior_deque.popleft())
            
    return answer

solution([1, 1, 9, 1, 1, 1], 0)