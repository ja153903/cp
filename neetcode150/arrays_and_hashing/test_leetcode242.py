from neetcode150.arrays_and_hashing.leetcode242 import Solution


def test_is_anagram():
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t) is True

    s = "rat"
    t = "car"
    assert solution.isAnagram(s, t) is False
