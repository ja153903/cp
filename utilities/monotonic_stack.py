from typing import List


def find_next_greater_element(nums: List[int]) -> int:
    stack = []
    n = len(nums)

    stack.append(nums[n - 1])

    for i in range(n - 2, -1, -1):
        while nums[i] < stack[-1]:
            stack.pop()

        stack.append(nums[i])
