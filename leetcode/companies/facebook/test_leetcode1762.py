import pytest

from .leetcode1762 import Solution


solution = Solution()


@pytest.mark.parametrize(
    "heights,expected",
    [([4, 2, 3, 1], [0, 2, 3]), ([4, 3, 2, 1], [0, 1, 2, 3]), ([1, 3, 2, 4], [3])],
)
def test_find_buildings(heights, expected):
    assert solution.findBuildings(heights) == expected
