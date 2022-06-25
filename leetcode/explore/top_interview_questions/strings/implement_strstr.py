class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i, ch in enumerate(haystack):
            if ch == needle[0] and self.is_substring(haystack, needle, i):
                return i

        return -1

    def is_substring(self, haystack: str, needle: str, i: int) -> bool:
        for j in range(len(needle)):
            if i + j >= len(haystack) or needle[j] != haystack[i + j]:
                return False

        return True
