from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        # iterate forwards on the temperatures
        for i, temperature in enumerate(temperatures):
            # while we have items on the stack we check if the current
            # value is greater than the top of the stack
            # if it is, then we continually adjust the number of days
            # until we get a higher temperature
            while stack and temperature > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx

            stack.append(i)

        return result
