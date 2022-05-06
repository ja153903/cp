from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        start, max_cnt, max_len = 0, 0, 0

        for end in range(len(s)):
            cnt[s[end]] += 1
            max_cnt = max(max_cnt, cnt[s[end]])

            while end - start + 1 - max_cnt > k:
                # this means we've replaced as many as we could
                cnt[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
