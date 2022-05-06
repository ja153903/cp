from neetcode150.two_pointers.leetcode167 import Solution

solution = Solution()


def test_two_sum():
    numbers = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(numbers, target) == [1, 2]
