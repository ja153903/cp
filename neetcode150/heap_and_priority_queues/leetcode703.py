import heapq
from typing import List


class KthLargest:
    """
    Note that this is only additive, we can create a min_heap here
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self._heap = []

        # The idea here is that if we keep k elements in a min heap
        # then the smallest element will be the kth largest element
        for num in nums:
            self._add(num)

    def _add(self, val: int) -> None:
        heapq.heappush(self._heap, val)
        if len(self._heap) > self.k:
            heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        self._add(val)

        return self._heap[0]
