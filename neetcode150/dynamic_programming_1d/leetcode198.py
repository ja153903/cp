from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

    def optimization(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(nums[i] + a, b)

        return b
