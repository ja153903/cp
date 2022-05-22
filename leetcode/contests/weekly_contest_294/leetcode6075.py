import heapq
from typing import List

from data_structures.priority_queue import PrioritizedItem


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additional_rocks: int
    ) -> int:
        heap = []
        bags = 0

        for cap, rock in zip(capacity, rocks):
            if cap == rock:
                bags += 1
            else:
                heapq.heappush(heap, PrioritizedItem(cap - rock, (cap, rock)))

        while additional_rocks > 0 and heap:
            front = heapq.heappop(heap)
            item = front.item

            diff = item[0] - item[1]

            if additional_rocks - diff >= 0:
                bags += 1
                additional_rocks -= diff

        return bags
