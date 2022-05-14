from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        self._backtrack(nums, [], result, 0)

        return result

    def _backtrack(
        self, nums: List[int], current: List[int], result: List[List[int]], start: int
    ) -> None:
        result.append(list(current))

        for i in range(start, len(nums)):
            current.append(nums[i])
            self._backtrack(nums, current, result, i + 1)
            current.pop()
