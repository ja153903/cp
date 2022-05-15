from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        self._backtrack(candidates, target, result, [], 0)

        return result

    def _backtrack(
        self,
        candidates: List[int],
        target: int,
        result: List[List[int]],
        current: List[int],
        start: int,
    ) -> None:
        if target <= 0:
            if target == 0:
                result.append(list(current))
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])
            self._backtrack(candidates, target - candidates[i], result, current, i + 1)
            current.pop()
