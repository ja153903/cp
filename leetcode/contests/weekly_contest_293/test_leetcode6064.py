import pytest

from .leetcode6064 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "bottom,top,special,expected", [(2, 9, [4, 6], 3), (6, 8, [7, 6, 8], 0)]
)
def test_solution(bottom, top, special, expected):
    assert solution.maxConsecutive(bottom, top, special) == expected
