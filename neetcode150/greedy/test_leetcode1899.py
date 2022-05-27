import pytest

from .leetcode1899 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "triplets,target,expected",
    [
        ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),
        ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),
        ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True),
        ([[1, 2, 1]], [1, 2, 1], True),
    ],
)
def test_merge_triplets(triplets, target, expected):
    assert solution.mergeTriplets(triplets, target) == expected
