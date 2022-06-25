from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs, key=len))
        prefix = []

        for i in range(min_len):
            curr = None
            for s in strs:
                if not curr:
                    curr = s[i]
                elif curr != s[i]:
                    return "".join(prefix)
            prefix.append(s[i])

        return "".join(prefix)
