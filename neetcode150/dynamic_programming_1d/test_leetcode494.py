import pytest

from .leetcode494 import Solution

solution = Solution()


@pytest.mark.parametrize("nums,target,expected", [([1, 1, 1, 1, 1], 3, 5)])
def test_find_target_sum_ways(nums, target, expected):
    assert solution.findTargetSumWays(nums, target) == expected
