from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = Counter(s)

        for ch in t:
            if ch not in counter or counter[ch] <= 0:
                return False

            counter[ch] -= 1

        return sum(counter.values()) == 0
