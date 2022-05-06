import pytest

from neetcode150.sliding_window.leetcode424 import Solution

solution = Solution()


@pytest.mark.parametrize(
    's,k,expected',
    [
        ('ABAB', 2, 4),
        ('AABABBA', 1, 4)
    ]
)
def test_character_replacement(s: str, k: int, expected: int):
    assert solution.characterReplacement(s, k) == expected
