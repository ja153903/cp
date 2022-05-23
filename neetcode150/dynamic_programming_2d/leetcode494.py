from typing import List, Dict, Tuple


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        We can try doing a brute force backtracking solution first
        and then see how we can optimize this

        Reference: https://leetcode.com/problems/target-sum/discuss/97335/Short-Java-DP-Solution-with-Explanation

        :param nums:
        :param target:
        :return:
        """
        memo = {}
        result = self._backtrack(nums, target, 0, 0, memo)

        return result

    def _backtrack(
        self,
        nums: List[int],
        target: int,
        i: int,
        path: int,
        memo: Dict[Tuple[int, int], int],
    ) -> int:
        # the optimization here is to keep track of the memo
        # for this we need to pick the proper keys
        # in our case, we want to use the index and the path sum
        # as our key
        if (i, path) in memo:
            return memo[(i, path)]

        if i == len(nums):
            if path == target:
                return 1
            return 0

        pos = self._backtrack(nums, target, i + 1, path + nums[i], memo)
        neg = self._backtrack(nums, target, i + 1, path - nums[i], memo)

        memo[(i, path)] = pos + neg

        return memo[(i, path)]
