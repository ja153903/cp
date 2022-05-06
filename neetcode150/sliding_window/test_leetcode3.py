import pytest

from neetcode150.sliding_window.leetcode3 import Solution

solution = Solution()


@pytest.mark.parametrize(
    's,expected',
    [('abcabcbb', 3), ('bbbbb', 1), ('pwwkew', 3)]
)
def test_length_of_longest_substring(s: str, expected: int):
    assert solution.lengthOfLongestSubstring(s) == expected
