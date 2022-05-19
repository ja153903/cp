import pytest

from .leetcode152 import Solution

solution = Solution()


@pytest.mark.parametrize("nums,expected", [([2, 3, -2, 4], 6), ([-2, 0, -1], 0)])
def test_max_product(nums, expected):
    assert solution.maxProduct(nums) == expected
