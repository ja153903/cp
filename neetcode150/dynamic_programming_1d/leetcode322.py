from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        You are given an integer array coins representing coins of different
        denominations and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount.
        If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.

        Approach:

        dp[i] ~ number of coins needed to get the amount.

        :param coins:
        :param amount:
        :return:
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # for each amount, you want to figure out the minimum
        # from all the coins that exist
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
