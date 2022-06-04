import pytest

from .leetcode408 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "word,abbr,expected",
    [("internationalization", "i12iz4n", True), ("apple", "a2e", False)],
)
def test_valid_word_abbreviation(word, abbr, expected):
    assert solution.validWordAbbreviation(word, abbr) == expected
