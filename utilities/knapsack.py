from typing import List

"""
What is a knapsack problem?

Given a set of items, each with a weight and a value, determine the number of each item to include in a collection
so that the total weight is less than or equal to a given limit and the total value is as large as possible.

0/1 Knapsack means that we either take the item or we don't. We can't partition the item in any way to accept part of it

What are the types of problems that would end up having to use this paradigm though?
* Problems where we have a set number of denominations that should hit a certain value like Coin Change 2 can be
  solved via knapsack algo
"""


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
