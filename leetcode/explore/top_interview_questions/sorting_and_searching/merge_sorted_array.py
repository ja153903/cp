from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        This problem is probably not the best way to do this since this is going to take
        O(n) space.

        TODO: Figure out a technique to optimize this to O(1) space.
        """
        result = []
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        for i in range(len(result)):
            nums1[i] = result[i]
