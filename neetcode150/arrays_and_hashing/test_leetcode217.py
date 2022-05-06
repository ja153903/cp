from neetcode150.arrays_and_hashing.leetcode217 import Solution


def test_contains_duplicate():
    nums = [1, 2, 3, 1]
    actual = Solution().containsDuplicate(nums)

    assert actual is True
