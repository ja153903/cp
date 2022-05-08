import pytest
from typing import List

from neetcode150.stack.leetcode739 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "temps,expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ],
)
def test_daily_temperatures(temps: List[int], expected: List[int]):
    assert solution.dailyTemperatures(temps) == expected
