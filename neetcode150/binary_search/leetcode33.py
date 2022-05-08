from typing import List

from utilities.binary_search import (
    find_min_in_sorted_pivoted_list,
    pivoted_binary_search,
)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx = find_min_in_sorted_pivoted_list(nums)
        return pivoted_binary_search(nums, target, min_idx)
