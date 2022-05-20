from typing import List


# TODO: Figure out how this applies to leetcode416.py
def knapsack(weights: List[int], profit: List[int], m: int) -> int:
    """
    The idea with 0/1 knapsack is that we want to maximize profit
    but under some weight constraint m.

    :param weights:
    :param profit:
    :param m:
    :return:
    """
    dp = [[0 for _ in range(m + 1)] for _ in range(len(weights) + 1)]

    # dp[i, w] = max(dp[i - 1, w], dp[i - 1, w - w[i]])
    for i in range(1, len(weights) + 1):
        for j in range(1, m + 1):
            if j - weights[i] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + profit[i])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]
