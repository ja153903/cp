from typing import List

import pytest

from neetcode150.stack.leetcode853 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "target,position,speed,expected",
    [(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3), (10, [3], [3], 1)],
)
def test_car_fleet(target: int, position: List[int], speed: List[int], expected: int):
    assert solution.carFleet(target, position, speed) == expected
