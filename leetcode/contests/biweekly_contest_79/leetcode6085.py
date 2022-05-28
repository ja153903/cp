import heapq
from typing import List

from data_structures.priority_queue import PrioritizedItem


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        importance = [0] * n

        for u, v in roads:
            indegree[u] += 1
            indegree[v] += 1

        max_heap = []

        for i, edges in enumerate(indegree):
            heapq.heappush(max_heap, PrioritizedItem(priority=-edges, item=i))

        for i in range(n, 0, -1):
            front = heapq.heappop(max_heap)
            item = front.item

            importance[item] = i

        result = 0

        for u, v in roads:
            result += importance[u] + importance[v]

        return result
