class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []

        for ch in s:
            if ch.isalnum():
                filtered.append(ch.lower())

        return filtered == filtered[::-1]
