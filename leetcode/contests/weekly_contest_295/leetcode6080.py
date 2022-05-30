from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        result = 0

        while True:
            to_remove = []

            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    to_remove.append(i)

            if not to_remove:
                break

            nums = [num for i, num in enumerate(nums) if i not in to_remove]

            result += 1

        return result
