from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        You are given an integer array coins representing coins of different denominations and an integer amount
        representing a total amount of money.

        Return the number of combinations that make up that amount.
        If that amount of money cannot be made up by any combination of the coins, return 0.

        You may assume that you have an infinite number of each kind of coin.

        The answer is guaranteed to fit into a signed 32-bit integer.

        Approach: this is a knapsack problem

        This is a knapsack problem because for some constraint (amount) we want to find out
        the number of ways we can fit the coin denominations into the knapsack while maximizing
        the number of unique combinations we can do this.

        :param amount:
        :param coins:
        :return:
        """
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1

        for i in range(1, len(coins) + 1):
            coin = coins[i - 1]
            dp[i][0] = 1

            for j in range(1, amount + 1):
                dp[i][j] += dp[i - 1][j]

                if j - coin >= 0:
                    dp[i][j] += dp[i][j - coin]

        return dp[-1][-1]

    def space_optimization(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amt in range(1, amount + 1):
                if amt - coin >= 0:
                    dp[amt] += dp[amt - coin]

        return dp[amount]
