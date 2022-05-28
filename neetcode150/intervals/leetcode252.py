from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i: (i[0], i[1]))

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            if prev[1] > curr[0]:
                return False

        return True
