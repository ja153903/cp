from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        We can try doing a brute force backtracking solution first
        and then see how we can optimize this

        for each index, we either make it negative or positive
        :param nums:
        :param target:
        :return:
        """
        result = self._backtrack(nums, target, 0, 0)

        return result

    def _backtrack(self, nums: List[int], target: int, i: int, path: int) -> int:
        if i == len(nums):
            if path == target:
                return 1
            return 0

        return self._backtrack(nums, target, i + 1, path + nums[i]) + self._backtrack(
            nums, target, i + 1, path - nums[i]
        )
