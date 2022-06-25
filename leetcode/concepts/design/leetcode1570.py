from collections import defaultdict
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self._vec = defaultdict(int)

        for i, num in enumerate(nums):
            if num != 0:
                self._vec[i] = num

    def dotProduct(self, vec: "SparseVector") -> int:
        this = self._vec
        other = vec._vec

        result = 0

        for key, value in this.items():
            if (other_value := other.get(key, 0)) != 0:
                result += value * other_value

        return result
