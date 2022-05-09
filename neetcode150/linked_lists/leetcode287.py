from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and uses only constant extra space.

        This problem requires us to use Floyd's Cycle Detection algorithm because
        we have a finite set here to itself.

        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return -1

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
