from typing import List, Set


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        visited = set()

        nums.sort()

        self._backtrack(nums, result, [], 0, visited)

        return result

    def _backtrack(
        self,
        nums: List[int],
        result: List[List[int]],
        current: List[int],
        start: int,
        visited: Set[str],
    ) -> None:
        current_hash = "".join([str(n) for n in current])

        if current_hash not in visited:
            result.append(list(current))
            visited.add(current_hash)

        for i in range(start, len(nums)):
            current.append(nums[i])
            self._backtrack(nums, result, current, i + 1, visited)
            current.pop()
