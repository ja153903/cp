import pytest

from neetcode150.sliding_window.leetcode76 import Solution

solution = Solution()


@pytest.mark.parametrize("s,t,expected", [("ADOBECODEBANC", "ABC", "BANC")])
def test_min_window(s: str, t: str, expected: str):
    assert solution.minWindow(s, t) == expected
