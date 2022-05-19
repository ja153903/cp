import pytest

from .leetcode647 import Solution

solution = Solution()


@pytest.mark.parametrize("s,expected", [("abc", 3), ("aaa", 6)])
def test_count_substrings(s: str, expected: int):
    assert solution.countSubstrings(s) == expected
