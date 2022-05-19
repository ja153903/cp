import pytest

from .leetcode139 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "s,word_dict,expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
def test_word_break(s, word_dict, expected):
    assert solution.wordBreak(s, word_dict) == expected
