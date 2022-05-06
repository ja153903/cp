from neetcode150.arrays_and_hashing.leetcode49 import Solution


def test_group_anagrams():
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    actual = solution.groupAnagrams(strs)
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    sorted_result = sorted([sorted(arr) for arr in actual], key=len)

    assert sorted_result == expected
