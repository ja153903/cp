from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        counter = Counter(nums1)

        for num in nums2:
            if num in counter and counter[num] > 0:
                result.append(num)
                counter[num] -= 1

        return result
