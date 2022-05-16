from collections import deque, defaultdict
from typing import List


def khan(num_nodes: int, adjacency_list: List[List[int]]):
    queue = deque()
    graph = defaultdict(list)
    indegree = [0 for _ in range(num_nodes)]

    for u, v in adjacency_list:
        indegree[u] += 1
        graph[v].append(u)

    for i, indeg in enumerate(indegree):
        if indeg == 0:
            queue.append(i)

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
