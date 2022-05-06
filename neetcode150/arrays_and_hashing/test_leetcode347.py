from neetcode150.arrays_and_hashing.leetcode347 import Solution


def test_top_kfrequent():
    solution = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert sorted(solution.topKFrequent(nums, k)) == [1, 2]
