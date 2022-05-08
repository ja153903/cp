import pytest
from typing import List

from neetcode150.stack.leetcode150 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "tokens,expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_solution(tokens: List[str], expected: int):
    assert solution.evalRPN(tokens) == expected
