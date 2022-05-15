import functools
import itertools
from typing import List


class Solution:
    # Reference: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/discuss/2039717/Check-Each-Bit
    def largestCombination(self, candidates: List[int]) -> int:
        """
        We want AND of some numbers to be > 0.
        Now when we want to do AND of some bits, the result will be 0 even if any one of those bits is 0.

        Ques: When can we get a result 0 when we do AND of two numbers?
        Ans: If all bits at same pos are opposite or both are 0, e.g - 1000 & 0110 = 0
        Conclusion: Thus, to get AND result non zero there must be a place i where bit is 1 in both numbers.

        And this same logic applies when we want to AND more than two numbers.
        So in this problem, we want to check how many numbers have 1 at the same position.

        :param candidates:
        :return:
        """
        return max(sum(n & (1 << i) > 0 for n in candidates) for i in range(0, 24))

    def tle(self, candidates: List[int]) -> int:
        result = (0, 0)

        for item in self._powerset(candidates):
            size = len(item)
            ans = functools.reduce(lambda a, b: a & b, item) if item else 0

            if ans > 0 and size > result[1]:
                result = (ans, size)

        return result[1]

    @staticmethod
    def _powerset(nums: List[int]):
        return itertools.chain.from_iterable(
            itertools.combinations(nums, r) for r in range(len(nums) + 1)
        )
