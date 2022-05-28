import pytest

from .leetcode56 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "intervals,expected",
    [([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])],
)
def test_merge(intervals, expected):
    assert solution.merge(intervals) == expected
