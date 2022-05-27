from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        result = []

        i = 0

        # add all intervals that end before the new one starts
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        # merge all overlapping intervals by mutating the current new_interval
        # in this case we can temporarily treat new_interval like the top result of our stack
        while i < len(intervals) and new_interval[1] >= intervals[i][0]:
            new_interval = [
                min(intervals[i][0], new_interval[0]),
                max(intervals[i][1], new_interval[1]),
            ]
            i += 1

        result.append(new_interval)

        for interval in intervals[i:]:
            result.append(interval)

        return result

    def brute_force(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        result = []

        intervals.append(new_interval)

        intervals.sort(key=lambda i: (i[0], i[1]))

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                top = result[-1]
                cur = interval

                if top[1] >= cur[0]:
                    result[-1] = [min(top[0], cur[0]), max(top[1], cur[1])]
                else:
                    result.append(interval)

        return result
