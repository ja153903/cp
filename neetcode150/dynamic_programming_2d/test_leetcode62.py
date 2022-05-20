import pytest

from .leetcode62 import Solution

solution = Solution()

test_cases = [(3, 7, 28), (3, 2, 3)]


@pytest.mark.parametrize("m,n,expected", test_cases)
def test_unique_paths(m: int, n: int, expected: int):
    assert solution.uniquePaths(m, n) == expected


@pytest.mark.parametrize("m,n,expected", test_cases)
def test_recursion(m: int, n: int, expected: int):
    assert solution.recursion(m, n) == expected
