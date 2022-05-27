from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. You are initially positioned at the array's first index,
        and each element in the array represents your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.

        :param nums:
        :return:
        """
        if len(nums) == 1:
            return True

        max_reach = 0

        for i in range(0, len(nums) - 1):
            # if the current index is greater than the max_reach
            # this means at some point we won't even be able to jump to i
            if i > max_reach:
                break

            max_reach = max(max_reach, nums[i] + i)

        return max_reach >= len(nums) - 1
