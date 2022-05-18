from typing import List


class Solution:
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        for i, value in enumerate(cost):
            if i < 2:
                dp[i] = value
            else:
                dp[i] = value + min(dp[i - 1], dp[i - 2])

        return min(dp[len(cost) - 1], dp[len(cost) - 2])
