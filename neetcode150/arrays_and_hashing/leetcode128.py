from typing import List

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in seen:
                i = num
                cnt = 0

                while i in seen:
                    cnt += 1
                    i += 1

                max_len = max(max_len, cnt)

        return max_len
