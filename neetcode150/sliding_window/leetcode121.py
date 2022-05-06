from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        profit = 0

        for end in prices[1:]:
            start = min(start, end)
            profit = max(profit, end - start)

        return profit
