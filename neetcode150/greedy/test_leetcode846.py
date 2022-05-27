import pytest

from .leetcode846 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "hand,group_size,expected",
    [
        ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
        ([1, 2, 3, 4, 5], 4, False),
        ([1, 2, 3, 4, 5, 6], 2, True),
    ],
)
def test_is_nstraight_hand(hand, group_size, expected):
    assert solution.isNStraightHand(hand, group_size) == expected
