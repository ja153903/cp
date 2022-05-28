import heapq
from typing import List

from data_structures.priority_queue import PrioritizedItem


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        importance = [0] * n

        # Count indegree/outdegree for each node
        # we count both because its bidirectional
        for u, v in roads:
            indegree[u] += 1
            indegree[v] += 1

        # Use heap to sort based on the number of edges coming into node
        max_heap = []

        for i, edges in enumerate(indegree):
            heapq.heappush(max_heap, PrioritizedItem(priority=-edges, item=i))

        # Assign importance based on max item from heap
        # Ties don't matter
        for i in range(n, 0, -1):
            front = heapq.heappop(max_heap)
            item = front.item

            importance[item] = i

        # Tabulate result
        result = 0

        for u, v in roads:
            result += importance[u] + importance[v]

        return result
