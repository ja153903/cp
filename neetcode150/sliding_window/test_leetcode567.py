import pytest

from neetcode150.sliding_window.leetcode567 import Solution

solution = Solution()


@pytest.mark.parametrize('s1,s2,expected', [('ab', 'eidbaooo', True), ('ab', 'eidboaoo', False)])
def test_check_inclusion(s1: str, s2: str, expected: bool):
    assert solution.checkInclusion(s1, s2) == expected
