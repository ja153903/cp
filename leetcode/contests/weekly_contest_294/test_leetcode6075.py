import pytest

from .leetcode6075 import Solution


solution = Solution()


@pytest.mark.parametrize(
    "capacity,rocks,additional_rocks,expected",
    [([2, 3, 4, 5], [1, 2, 4, 4], 2, 3), ([10, 2, 2], [2, 2, 0], 100, 3)],
)
def test_maximum_bags(capacity, rocks, additional_rocks, expected):
    assert solution.maximumBags(capacity, rocks, additional_rocks) == expected
