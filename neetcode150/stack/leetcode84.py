from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Dope explanation:
        https://abhinandandubey.github.io/posts/2019/12/15/Largest-Rectangle-In-Histogram.html

        :param heights:
        :return:
        """
        stack = [-1]
        largest_area = 0

        heights.append(0)

        for i, height in enumerate(heights):
            # if the top of the stack is greater than the current height
            # we're iterating on, then this means we should
            # remove that value from the top of the stack since we can't use that anymore
            # but we want to see what could have been
            while heights[stack[-1]] > heights[i]:
                last = stack.pop()
                h = heights[last]
                w = i - stack[-1] - 1

                largest_area = max(largest_area, h * w)

            stack.append(i)

        heights.pop()

        return largest_area
