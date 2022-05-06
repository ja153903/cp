import pytest
from typing import List

from neetcode150.sliding_window.leetcode239 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]), ([1], 1, [1])],
)
def test_max_sliding_window(nums: List[int], k: int, expected: List[int]):
    assert solution.maxSlidingWindow(nums, k) == expected
