import pytest

from neetcode150.stack.leetcode20 import Solution

solution = Solution()


@pytest.mark.parametrize("s,expected", [("()", True), ("()[]{}", True), ("(]", False)])
def test_is_valid(s: str, expected: bool):
    assert solution.isValid(s) == expected
