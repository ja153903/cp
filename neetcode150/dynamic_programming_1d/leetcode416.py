import functools
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Given a non-empty array nums containing only positive integers, find if the array can be partitioned
        into two subsets such that the sum of elements in both subsets is equal.

        This problem is apparently 0/1 knapsack - I still don't really understand how 0/1 knapsack works

        TODO: Still unclear about how this problem works.

        Reference:
        https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask

        0/1 Knapsack Reference:
        https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation

        :param nums:
        :return:
        """
        rs = sum(nums)

        if rs & 1 == 1:
            return False

        rs = rs // 2

        dp = [False] * (rs + 1)
        dp[0] = True

        for num in nums:
            for i in range(rs, num - 1, -1):
                if i >= num:
                    dp[i] |= dp[i - num]

        return dp[rs]

    def recursion(self, nums: List[int]) -> bool:
        """
        How do we solve this problem recursively?

        Base case, if the i we're iterating on is the length of the list, then we're done
        we should check if the sums we're collecting are equal

        Otherwise, we either add the current number to the left or right sum

        Time complexity: O(2^n)

        :param nums:
        :return:
        """

        @functools.cache
        def _recurse(left: int, right: int, i: int) -> bool:
            if i >= len(nums):
                return left == right

            return _recurse(left + nums[i], right, i + 1) or _recurse(
                left, right + nums[i], i + 1
            )

        return _recurse(0, 0, 0)
