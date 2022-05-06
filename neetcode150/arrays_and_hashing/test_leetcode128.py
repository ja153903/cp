from neetcode150.arrays_and_hashing.leetcode128 import Solution

solution = Solution()


def test_longest_consecutive():
    nums = [100, 4, 200, 1, 3, 2]
    assert solution.longestConsecutive(nums) == 4
