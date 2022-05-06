from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # this is a more traditional sliding window problem
        # that we should definitely extract into a template
        # we want to find the smallest such substring that contains
        # all the characters of t
        if len(s) < len(t):
            return ""

        counter = defaultdict(int)
        start, min_start, min_len, target = 0, 0, float("inf"), len(t)

        for ch in t:
            counter[ch] += 1

        for end, ch in enumerate(s):
            counter[ch] -= 1

            if counter[ch] >= 0:
                target -= 1

            while target == 0:
                current_window_size = end - start + 1
                if current_window_size < min_len:
                    min_start = start
                    min_len = current_window_size

                counter[s[start]] += 1
                if counter[s[start]] > 0:
                    target += 1

                start += 1

        return s[min_start : min_start + min_len] if min_len != float("inf") else ""
