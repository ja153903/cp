import pytest

from .leetcode70 import Solution

solution = Solution()


@pytest.mark.parametrize("n,expected", [(2, 2), (3, 3)])
def test_recursive(n: int, expected: int):
    assert solution.recursive(n) == expected


@pytest.mark.parametrize("n,expected", [(2, 2), (3, 3)])
def test_climb_stairs(n: int, expected: int):
    assert solution.climbStairs(n) == expected
