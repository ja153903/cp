from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self._robber(nums[1:]), self._robber(nums[:-1]))

    def _robber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(nums[i] + a, b)

        return b
