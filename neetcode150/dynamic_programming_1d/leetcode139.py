from typing import List


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_set = set(word_dict)

        # dp[i] ~ up to index i (not including it) we denote if its possible to be made up of words
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # if the previous j is true and the current substring is in the list
                # then we know that we can create a word up to index i
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]
