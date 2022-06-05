from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while len(nums) > 1:
            result, i, should_get_min = [], 0, True

            while i < len(nums):
                if should_get_min:
                    result.append(min(nums[i + 1], nums[i]))
                else:
                    result.append(max(nums[i + 1], nums[i]))

                should_get_min = not should_get_min
                i += 2

            nums = result

        return nums[-1]
