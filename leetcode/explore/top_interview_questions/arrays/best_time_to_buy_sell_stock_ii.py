from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can greedily do something about this
        result = 0
        _min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > _min:
                result += prices[i] - _min

            _min = prices[i]

        return result
