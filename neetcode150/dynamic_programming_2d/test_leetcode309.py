import pytest

from .leetcode309 import Solution

solution = Solution()


@pytest.mark.parametrize("nums,expected", [([1, 2, 3, 0, 2], 3), ([1], 0), ([2, 1], 0)])
def test_max_profit(nums, expected):
    assert solution.maxProfit(nums) == expected
