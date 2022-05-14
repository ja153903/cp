import pytest

from .leetcode1046 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "weight,expected", [([2, 7, 4, 1, 8, 1], 1), ([1], 1), ([2, 2], 0)]
)
def test_last_stone_weight(weight, expected):
    assert solution.lastStoneWeight(weight) == expected
