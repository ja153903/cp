from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This question screams finding the next greater element
        # If this is the case, then we should use a monotonic stack.
        result = [0] * len(temperatures)
        stack = []

        # iterate forwards on the temperatures
        for i, temperature in enumerate(temperatures):
            # while we have items on the stack we check if the current
            # value is greater than the top of the stack
            # if it is, then we continually adjust the number of days
            # until we get a higher temperature
            # Why do we continually pop the element on the stack?
            # When we pop the item off the stack, we do it because
            # we've found the next greater element. So we have to go through the
            # entire stack to update this information
            while stack and temperature > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx

            stack.append(i)

        return result
