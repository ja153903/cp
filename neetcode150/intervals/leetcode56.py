from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals.sort(key=lambda i: (i[0], i[1]))

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                top = result[-1]

                if top[1] >= interval[0]:
                    result[-1] = [min(top[0], interval[0]), max(top[1], interval[1])]
                else:
                    result.append(interval)

        return result
