import pytest

from .leetcode53 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,expected", [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([5, 4, -1, 7, 8], 23)]
)
def test_max_sub_array(nums, expected):
    assert solution.maxSubArray(nums) == expected
