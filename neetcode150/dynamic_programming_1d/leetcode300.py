from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Find the longest increasing sequence in a list.

        What is brute force approach here? we'd have to recursively
        enumerate all possible ways to get to the next number

        Suppose we have the following example: [0, 1, 0, 3, 2, 3]

        For every digit, we'd spawn a dfs to look forward to the next possible
        longest increasing sequence.

        How can we use DP to optimize this solution?

        dp[i] ~ the longest possible sequence up to index i (including the current index)

        dp[0] ~ should just be 1

        dp[i] = max(dp[i], dp[j])

        :param nums:
        :return:
        """
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
