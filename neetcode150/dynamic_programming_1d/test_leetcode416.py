import pytest

from .leetcode416 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,expected", [([1, 5, 11, 5], True), ([1, 2, 3, 5], False), ([], True)]
)
def test_recursion(nums, expected):
    assert solution.recursion(nums) == expected


@pytest.mark.parametrize(
    "nums,expected",
    [([1, 5, 11, 5], True), ([1, 2, 3, 5], False), ([], True), ([3, 3, 3, 4, 5], True)],
)
def test_canPartition(nums, expected):
    assert solution.canPartition(nums) == expected
