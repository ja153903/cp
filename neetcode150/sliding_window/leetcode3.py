class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        start = 0
        longest_substr_len = 0

        for end, ch in enumerate(s):
            if ch in found:
                start = max(start, found[ch] + 1)

            longest_substr_len = max(longest_substr_len, end - start + 1)
            found[ch] = end

        return longest_substr_len
