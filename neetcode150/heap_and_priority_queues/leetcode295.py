import heapq


class MedianFinder:
    """
    The approach here is to implement two heaps.
    One heap will always have size k
    The other heap will have size either k or k + 1

    The smaller heap will be a max heap of the smaller values
    The larger heap will be a min heap of the larger values

    if the length of both heaps are the same, then we should push the value into the smaller heap
    and then pop the value out from there and push it into the larger heap

    Otherwise, we do the opposite operations.
    """

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            # we subtract here because the values in small are negative
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
