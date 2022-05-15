from collections import deque
from typing import List


PHONE_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        queue = deque()
        queue.append("")

        for digit in digits:
            size = len(queue)
            for _ in range(size):
                front = queue.popleft()

                for ch in PHONE_MAP[digit]:
                    queue.append(f"{front}{ch}")

        return list(queue)
