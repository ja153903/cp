from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # every element appears twice except for one
        result = 0

        # the idea here is that we can do x ^ y for every element
        # given that XOR is commutative, we know that x ^ x ^ y == x ^ y ^ x
        # we also know that x ^ x == 0
        # so in the end, we'll get the number that isn't duplicated as
        # we get rid of all the values that are by zeroing them out
        for num in nums:
            result ^= num

        return result
