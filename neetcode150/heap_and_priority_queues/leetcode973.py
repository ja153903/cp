import heapq
from typing import List

from data_structures.priority_queue import PrioritizedItem


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heapq.heappush(
                heap, PrioritizedItem(priority=-(x * x + y * y), item=[x, y])
            )
            if len(heap) > k:
                heapq.heappop(heap)

        return [pi.item for pi in heap]
