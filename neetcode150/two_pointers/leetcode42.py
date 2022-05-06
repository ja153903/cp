from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxleft, maxright = height[left], height[right]
        result = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > maxleft:
                    maxleft = height[left]
                else:
                    result += maxleft - height[left]

                left += 1
            else:
                if height[right] > maxright:
                    maxright = height[right]
                else:
                    result += maxright - height[right]

                right -= 1

        return result
