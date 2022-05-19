from typing import List


class Solution:
    # solve this with Kadane's algorithm modified for multiplication
    # what this means is that we should take into consideration
    # the minimum value as well since the product of two negative numbers
    # could end up producing a larger product
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far, max_so_far = nums[0], nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            min_so_far, max_so_far = min(
                min_so_far * nums[i], nums[i], max_so_far * nums[i]
            ), max(min_so_far * nums[i], nums[i], max_so_far * nums[i])

            current_max = max(current_max, min_so_far, max_so_far)

        return current_max
