from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []

        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        starts.sort()
        ends.sort()

        result = 0
        end_itr = 0

        for i in range(len(starts)):
            if starts[i] < ends[end_itr]:
                result += 1
            else:
                end_itr += 1

        return result
