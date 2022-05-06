from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indices = deque()
        result = []

        for end, num in enumerate(nums):
            # keep track of current window
            # if front index is not within the window, we can get rid of it
            while indices and indices[0] <= end - k:
                indices.popleft()

            # if the last item in the index is less than the current num
            # then we can get rid of it
            while indices and nums[indices[-1]] <= num:
                indices.pop()

            indices.append(end)

            # once we have a window of size k, we can start adding values
            # to our result list
            if end - k + 1 >= 0:
                result.append(nums[indices[0]])

        return result
