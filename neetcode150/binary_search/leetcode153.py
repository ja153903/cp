from typing import List

from utilities.binary_search import find_min_in_sorted_pivoted_list


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = find_min_in_sorted_pivoted_list(nums)

        return nums[i]
