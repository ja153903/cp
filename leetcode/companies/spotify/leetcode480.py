from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []

        for i in range(k - 1, len(nums)):
            slc = sorted(nums[i - k + 1 : i + 1])
            mid = k // 2
            if len(slc) % 2 == 0:
                result.append((slc[mid] + slc[mid - 1]) / 2)
            else:
                result.append(slc[mid] * 1.0)

        return result

    # TODO: Finish this problem
    def optimal(self, nums: List[int], k: int) -> List[float]:
        pass
