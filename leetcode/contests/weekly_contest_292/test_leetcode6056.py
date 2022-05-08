import pytest

from leetcode.contests.weekly_contest_292.leetcode6056 import Solution


solution = Solution()


@pytest.mark.parametrize(
    "num,expected", [("6777133339", "777"), ("2300019", "000"), ("42352338", "")]
)
def test_largest_good_integer(num: str, expected: str):
    assert solution.largestGoodInteger(num) == expected
