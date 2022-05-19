class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""

        for i in range(len(s)):
            odd_s = self.extend(s, i, i)
            even_s = self.extend(s, i, i + 1)

            max_palindrome = max(max_palindrome, odd_s, even_s, key=len)

        return max_palindrome

    def extend(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]
