import pytest

from .leetcode45 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([2, 3, 1, 1, 4], 2),
        ([0], 0),
        ([1, 2, 1, 1, 1], 3),
    ],
)
def test_jump(nums, expected):
    assert solution.jump(nums) == expected
