from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        result, i = 0, 1
        cur_min = nums[0]

        while i < len(nums):
            if i < len(nums) and nums[i] - cur_min <= k:
                i += 1
                continue

            result += 1

            if i < len(nums):
                cur_min = nums[i]

            i += 1

        return result + 1
