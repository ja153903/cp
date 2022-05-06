from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1

                while j < k:
                    current = nums[j] + nums[k]
                    target = -nums[i]

                    if current == target:
                        result.append([nums[i], nums[j], nums[k]])

                        while j < k and nums[j] == nums[j + 1]:
                            j += 1

                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1

                        j += 1
                        k -= 1
                    elif current < target:
                        j += 1
                    else:
                        k -= 1

        return result
