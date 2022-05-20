from typing import List

import pytest

from neetcode150.two_pointers.leetcode42 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "height,expected",
    [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), ([4, 2, 0, 3, 2, 5], 9)],
)
def test_solution(height: List[int], expected: int):
    assert solution.trap(height) == expected
