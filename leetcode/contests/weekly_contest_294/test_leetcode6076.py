import pytest

from .leetcode6076 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "stock_prices,expected",
    [
        ([[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]], 3),
        ([[3, 4], [1, 2], [7, 8], [2, 3]], 1),
    ],
)
def test_minimum_lines(stock_prices, expected):
    assert solution.minimumLines(stock_prices) == expected
