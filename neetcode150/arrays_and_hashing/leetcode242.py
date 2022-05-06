from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)

        for ch in t:
            if ch not in s_counter:
                return False

            s_counter[ch] -= 1

        return all([value == 0 for value in s_counter.values()])
