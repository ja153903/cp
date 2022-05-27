import pytest

from .leetcode678 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "s,expected",
    [("(*))", True), ("(**))(*", True), ("(*)", True), ("()", True), ("))**", False)],
)
def test_check_valid_string(s, expected):
    assert solution.checkValidString(s) == expected
