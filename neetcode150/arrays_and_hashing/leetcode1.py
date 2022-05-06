from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            if (cur := target - val) in seen:
                return [seen[cur], i]

            seen[val] = i

        return []
