from neetcode150.two_pointers.leetcode15 import Solution

solution = Solution()


def test_three_sum():
    nums = [-1, 0, 1, 2, -1, -4]
    assert solution.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
