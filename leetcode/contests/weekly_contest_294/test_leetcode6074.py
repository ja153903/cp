import pytest


from .leetcode6074 import Solution

solution = Solution()


@pytest.mark.parametrize("s,letter,expected", [("foobar", "o", 33)])
def test_percentage_letter(s, letter, expected):
    assert solution.percentageLetter(s, letter) == expected
