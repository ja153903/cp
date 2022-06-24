import pytest

from .best_time_to_buy_sell_stock_ii import Solution


solution = Solution()


@pytest.mark.parametrize(
    "prices,expected",
    [([7, 1, 5, 3, 6, 4], 7), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0)],
)
def test_max_profit(prices, expected):
    assert solution.maxProfit(prices) == expected
