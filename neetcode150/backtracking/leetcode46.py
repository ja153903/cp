from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations.
        You can return the answer in any order.

        NOTE: if the problem didn't have the restriction of distinct integers, we can
        use the indices as a way to uniquely identify them.

        :param nums:
        :return:
        """
        result = []

        self._backtrack(nums, result, [], set())

        return result

    def _backtrack(
        self,
        nums: List[int],
        result: List[List[int]],
        current: List[int],
        visited: Set[int],
    ) -> None:
        if len(current) == len(nums):
            result.append(list(current))
        else:
            for num in nums:
                if num in visited:
                    continue

                visited.add(num)
                current.append(num)
                self._backtrack(nums, result, current, visited)
                visited.remove(num)
                current.pop()
