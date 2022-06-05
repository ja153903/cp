import pytest

from .leetcode6091 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [([3, 6, 1, 2, 5], 2, 2), ([1, 2, 3], 1, 2), ([2, 2, 4, 5], 0, 3)],
)
def test_partition_array(nums, k, expected):
    assert solution.partitionArray(nums, k) == expected
