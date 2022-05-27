import pytest

from .leetcode55 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False), ([1, 0, 1, 0], False)],
)
def test_can_jump(nums, expected):
    assert solution.canJump(nums) == expected
