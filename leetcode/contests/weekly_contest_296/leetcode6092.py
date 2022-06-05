from collections import defaultdict
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # key -> num, value -> index
        hash = defaultdict(int)

        for i, num in enumerate(nums):
            hash[num] = i

        for cur, new in operations:
            # find pos of cur
            pos = hash[cur]
            nums[pos] = new
            hash[new] = pos
            hash[cur] = -1

        return nums
