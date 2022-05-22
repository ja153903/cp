from typing import List


class Solution:
    @staticmethod
    def slope(p1: List[int], p2: List[int]) -> float:
        rise = p2[1] - p1[1]
        run = p2[0] - p1[0]

        return rise / run

    def minimumLines(self, stock_prices: List[List[int]]) -> int:
        if len(stock_prices) == 1:
            return 0

        if len(stock_prices) == 2:
            return 1

        stock_prices.sort(key=lambda sp: (sp[0], sp[1]))

        result = 1

        prev = self.slope(stock_prices[0], stock_prices[1])

        for i in range(2, len(stock_prices)):
            curr = self.slope(stock_prices[i - 1], stock_prices[i])

            if curr != prev:
                result += 1

            prev = curr

        return result
