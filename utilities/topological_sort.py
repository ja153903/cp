from collections import deque, defaultdict
from typing import List


def khan(num_nodes: int, adjacency_list: List[List[int]]):
    queue = deque()
    graph = defaultdict(list)
    indegree = [0 for _ in range(num_nodes)]

    for dst, src in adjacency_list:
        indegree[dst] += 1
        graph[src].append(dst)

    for i, indeg in enumerate(indegree):
        if indeg == 0:
            queue.append(i)

    while queue:
        removed_node = queue.popleft()

        for next_node in graph[removed_node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
