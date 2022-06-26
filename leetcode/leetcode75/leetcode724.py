from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1] + num)

        for i, num in enumerate(prefix):
            if i == 0:
                if prefix[-1] - nums[0] == 0:
                    return i
            elif i == len(prefix) - 1:
                if prefix[-1] - nums[-1] == 0:
                    return i
            else:
                if prefix[-1] - prefix[i] == prefix[i - 1]:
                    return i

        return -1
