# DFS구현(그래프 자료구조)
def dfs(graph, start_v, visited=[]):
    visited.append(start_v)
    for v in graph[start_v]:
        if v not in visited:
            visited = dfs(graph, v, visited)
        return visited

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A'],
}

dfs(graph, 'A')