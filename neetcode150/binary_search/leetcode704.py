from typing import List

from utilities.binary_search import binary_search


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)
