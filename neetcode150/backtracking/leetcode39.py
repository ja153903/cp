from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        self._backtrack(candidates, target, [], result, 0)

        return result

    def _backtrack(
        self,
        candidates: List[int],
        target: int,
        current: List[int],
        result: List[List[int]],
        start: int,
    ) -> None:
        if target <= 0:
            if target == 0:
                result.append(list(current))
            return
        else:
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if target - candidate >= 0:
                    current.append(candidate)
                    self._backtrack(candidates, target - candidate, current, result, i)
                    current.pop()
