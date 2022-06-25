from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        # dp[i] ~ maximum amount of money you can make without alerting the police
        # if there is only 1 house, then the amount you get from the first house is your result
        # if there are two houses, then it's going to be the maximum between the first two
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
