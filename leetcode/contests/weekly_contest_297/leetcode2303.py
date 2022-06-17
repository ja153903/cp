from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0

        for i, bracket in enumerate(brackets):
            upper, percent = bracket
            percent_as_float = percent / 100.0

            if i == 0:
                amount = min(income, upper)
            else:
                amount = min(upper - brackets[i - 1][0], income)

            result += amount * percent_as_float
            income -= amount

        return result
