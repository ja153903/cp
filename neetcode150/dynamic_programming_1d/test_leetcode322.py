import pytest

from .leetcode322 import Solution

solution = Solution()


@pytest.mark.parametrize("coins,amount,expected", [([1, 2, 5], 11, 3)])
def test_coin_change(coins, amount, expected):
    assert solution.coinChange(coins, amount) == expected
