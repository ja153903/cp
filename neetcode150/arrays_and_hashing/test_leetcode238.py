from neetcode150.arrays_and_hashing.leetcode238 import Solution

solution = Solution()


def test_product_except_self():
    nums = [1, 2, 3, 4]

    expected = [24, 12, 8, 6]
    actual = solution.productExceptSelf(nums)

    assert expected == actual

    nums = [-1, 1, 0, -3, 3]

    expected = [0, 0, 9, 0, 0]
    actual = solution.productExceptSelf(nums)

    assert expected == actual
