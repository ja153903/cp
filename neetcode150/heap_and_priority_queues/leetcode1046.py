import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heapq.heappush(heap, -weight)

        while len(heap) >= 2:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first == second:
                continue

            heapq.heappush(heap, -abs(first - second))

        return -heap[0] if heap else 0
