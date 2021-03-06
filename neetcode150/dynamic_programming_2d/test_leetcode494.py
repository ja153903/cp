import pytest

from neetcode150.dynamic_programming_2d.leetcode494 import Solution

solution = Solution()


@pytest.mark.parametrize("nums,target,expected", [([1, 1, 1, 1, 1], 3, 5)])
def test_backtracking_solution(nums, target, expected):
    assert solution.findTargetSumWays(nums, target) == expected
