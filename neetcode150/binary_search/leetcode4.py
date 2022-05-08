from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Based on the following LeetCode discussion:
        # https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation
        n1, n2 = len(nums1), len(nums2)

        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)

        # note that n2 will always be less than n1
        # why do we do n2 * 2 here?
        # since n2 will at most the size of n1, if we do
        # twice the size of n2, then this is at most twice of n1
        left, right = 0, n2 * 2

        while left <= right:
            mid2 = left + (right - left) // 2
            mid1 = n1 + n2 - mid2

            l1 = float("-inf") if mid1 == 0 else nums1[(mid1 - 1) // 2]
            l2 = float("-inf") if mid2 == 0 else nums2[(mid2 - 1) // 2]
            r1 = float("inf") if mid1 == n1 * 2 else nums1[mid1 // 2]
            r2 = float("inf") if mid2 == n2 * 2 else nums2[mid2 // 2]

            if l1 > r2:
                left = mid2 + 1
            elif l2 > r1:
                right = mid2 - 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2

        return -1

    @staticmethod
    def brute_force(nums1: List[int], nums2: List[int]) -> float:
        result = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        mid = len(result) // 2
        if len(result) % 2 == 0:
            return (result[mid] + result[mid - 1]) // 2

        return result[mid]
