from neetcode150.two_pointers.leetcode11 import Solution

solution = Solution()


def test_max_area():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height) == 49
