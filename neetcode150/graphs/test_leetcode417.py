import pytest

from .leetcode417 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "heights,expected",
    [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        )
    ],
)
def test_pacific_atlantic(heights, expected):
    assert (
        sorted(solution.pacificAtlantic(heights), key=lambda item: (item[0], item[1]))
        == expected
    )
