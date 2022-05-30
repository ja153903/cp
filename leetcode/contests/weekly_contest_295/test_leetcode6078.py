import pytest

from .leetcode6078 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "s,target,expected",
    [("ilovecodingonleetcode", "code", 2), ("abbaccaddaeea", "aaaaa", 1)],
)
def test_rearrange_characters(s, target, expected):
    assert solution.rearrangeCharacters(s, target) == expected
