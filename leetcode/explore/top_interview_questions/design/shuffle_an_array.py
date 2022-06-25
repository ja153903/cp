from random import randrange
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        clone = self.nums[:]

        for i in range(len(clone) - 1, 0, -1):
            j = randrange(0, i + 1)
            clone[i], clone[j] = clone[j], clone[i]

        return clone
