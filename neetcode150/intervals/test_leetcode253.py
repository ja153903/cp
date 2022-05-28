import pytest

from .leetcode253 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[9, 10], [4, 9], [4, 17]], 2),
    ],
)
def test_min_meeting_rooms(intervals, expected):
    assert solution.minMeetingRooms(intervals) == expected
