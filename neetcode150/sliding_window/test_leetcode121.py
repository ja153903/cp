import pytest

from neetcode150.sliding_window.leetcode121 import Solution

solution = Solution()


@pytest.mark.parametrize(
    'prices,expected',
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]
)
def test_max_profit(prices, expected):
    assert solution.maxProfit(prices) == expected
