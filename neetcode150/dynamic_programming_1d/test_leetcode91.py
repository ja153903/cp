import pytest

from .leetcode91 import Solution

solution = Solution()


@pytest.mark.parametrize("s,expected", [("12", 2), ("226", 3)])
def test_num_decodings(s: str, expected: int):
    assert solution.numDecodings(s) == expected
