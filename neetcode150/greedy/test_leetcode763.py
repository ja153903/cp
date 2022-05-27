import pytest

from .leetcode763 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "s,expected", [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10])]
)
def test_partition_labels(s, expected):
    assert solution.partitionLabels(s) == expected
