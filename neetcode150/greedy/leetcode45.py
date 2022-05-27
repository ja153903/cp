from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

        Each element in the array represents your maximum jump length at that position.

        Your goal is to reach the last index in the minimum number of jumps.

        You can assume that you can always reach the last index.

        :param nums:
        :return:
        """
        steps, reach, optimal_reach = 0, 0, 0

        # NOTE: we don't include the last element in our iteration because
        # that is our goal, so it doesn't help in our calculation
        for i, num in enumerate(nums[:-1]):
            # figure out what the max reach is
            reach = max(reach, i + num)

            # if we've landed on the optimal_reach
            # then we have to update the number of steps we take
            # as well as update our optimal_reach to the furthest reach
            # we have so far.
            # Note that compared to Jump Game I, we don't care to exit early
            # if we've found a bad jump because we're guaranteed to always reach
            # the end of the list
            if i == optimal_reach:
                steps += 1
                optimal_reach = reach

        return steps
