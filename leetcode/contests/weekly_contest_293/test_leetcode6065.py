import pytest

from .leetcode6065 import Solution

solution = Solution()


@pytest.mark.parametrize("candidates,expected", [([16, 17, 71, 62, 12, 24, 14], 4)])
def test_largest_combination(candidates, expected):
    assert solution.largestCombination(candidates) == expected
