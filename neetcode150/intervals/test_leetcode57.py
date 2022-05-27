import pytest

from .leetcode57 import Solution


solution = Solution()


@pytest.mark.parametrize(
    "intervals,new_interval,expected",
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
        ([[1, 5]], [0, 0], [[0, 0], [1, 5]]),
    ],
)
def test_insert(intervals, new_interval, expected):
    assert solution.insert(intervals, new_interval) == expected
