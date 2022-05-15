import heapq
from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        """
        Turn special into a minheap
        we keep track of current which starts at bottom and ends when we reach top or heap is empty
        pop the min value from heap and see where we can set up the first boundary

        :param bottom:
        :param top:
        :param special:
        :return:
        """
        heapq.heapify(special)
        current = bottom

        result = 0

        while special:
            value = heapq.heappop(special)

            result = max(result, value - current)
            current = value + 1

        if current < top:
            result = max(result, top - current + 1)

        return result
