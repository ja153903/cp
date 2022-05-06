from collections import defaultdict
from typing import DefaultDict


def _all_zero(counter: DefaultDict[int, int]) -> bool:
    for value in counter.values():
        if value != 0:
            return False

    return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counter = defaultdict(int)

        for i in range(len(s1)):
            counter[s1[i]] += 1
            counter[s2[i]] -= 1

        if _all_zero(counter):
            return True

        for i in range(len(s1), len(s2)):
            counter[s2[i]] -= 1
            # this updates the window counter
            counter[s2[i - len(s1)]] += 1
            if _all_zero(counter):
                return True

        return False
