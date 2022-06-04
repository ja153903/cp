from collections import defaultdict
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self._vec = defaultdict(int)

        for i, num in enumerate(nums):
            if num != 0:
                self._vec[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0

        for key, value in vec._vec.items():
            if key not in self._vec:
                continue

            result += value * self._vec[key]

        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
