import pytest
from typing import List

from .leetcode746 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "cost,expected", [([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)]
)
def test_minCostClimbingStairs(cost: List[int], expected: int):
    assert solution.minCostClimbingStairs(cost) == expected
