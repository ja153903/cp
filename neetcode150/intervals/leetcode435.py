from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Suppose we have a list called intervals where intervals[i] = [start_i, end_i],
        return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

        Approach:

        Instead of finding the minimum number of intervals directly, we should find the longest number of non-overlapping
        intervals and subtract that from the number of intervals.

        This problem then boils down to interval scheduling.

        :param intervals:
        :return:
        """
        n = len(intervals)

        intervals.sort(key=lambda i: i[1])

        path = 1
        prev = intervals[0]

        for i in range(1, len(intervals)):
            cur = intervals[i]

            if prev[1] <= cur[0]:
                path += 1
                prev = cur

        return n - path
