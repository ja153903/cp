from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve. You may complete as many transactions as you like
        (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

        After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
        Note: You may not engage in multiple transactions simultaneously
        (i.e., you must sell the stock before you buy again).

        Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)

        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0

        can_buy = [0] * len(prices)
        can_sell = [0] * len(prices)
        cooldown = [0] * len(prices)

        can_sell[0] = -prices[0]
        cooldown[0] = float("-inf")

        for i in range(1, len(prices)):
            # the buying state is either the previous buying state since we didnt do anything
            # or it could have been from the previous resting state
            can_buy[i] = max(can_buy[i - 1], cooldown[i - 1])
            # To get to the selling state, we either held and did not have to cooldown or we take
            # the profit from the last time we bought and subtract by the price we're buying at
            can_sell[i] = max(can_sell[i - 1], can_buy[i - 1] - prices[i])
            # The only way to get to the resting state is to have sold from the previous state
            # so here we add the previous max profit as we're going to sell and then adding the price
            cooldown[i] = can_sell[i - 1] + prices[i]

        return max(can_buy[-1], cooldown[-1])
