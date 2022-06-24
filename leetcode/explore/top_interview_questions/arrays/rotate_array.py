from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Downside to this solution is that we use O(n) space
        """
        n = len(nums)
        copy = list(nums)

        for i, num in enumerate(copy):
            nums[(i + k) % n] = copy[i]

    def rotate_by_reversing(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # reverse the array
        n = len(nums)
        k %= n

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
