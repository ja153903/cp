from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        idx = 0

        for i, num in enumerate(nums):
            if num not in seen:
                nums[idx] = num
                idx += 1

                seen.add(num)

        return idx
