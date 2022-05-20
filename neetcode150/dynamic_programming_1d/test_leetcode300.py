import pytest

from .leetcode300 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
    ],
)
def test_length_of_lis(nums, expected):
    assert solution.lengthOfLIS(nums) == expected
