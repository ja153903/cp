import pytest

from .leetcode435 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
        (
            [
                [-52, 31],
                [-73, -26],
                [82, 97],
                [-65, -11],
                [-62, -49],
                [95, 99],
                [58, 95],
                [-31, 49],
                [66, 98],
                [-63, 2],
                [30, 47],
                [-40, -26],
            ],
            7,
        ),
    ],
)
def test_erase_overlap_intervals(intervals, expected):
    assert solution.eraseOverlapIntervals(intervals) == expected
