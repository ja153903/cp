import pytest
from typing import List

from neetcode150.stack.leetcode84 import Solution

solution = Solution()


@pytest.mark.parametrize("heights,expected", [([2, 1, 5, 6, 2, 3], 10)])
def test_solution(heights: List[int], expected: int):
    assert solution.largestRectangleArea(heights) == expected
