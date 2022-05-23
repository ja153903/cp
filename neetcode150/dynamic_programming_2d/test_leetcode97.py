import pytest

from .leetcode97 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "s1,s2,s3,expected",
    [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ],
)
def test_is_interleave(s1, s2, s3, expected):
    assert solution.isInterleave(s1, s2, s3) == expected
