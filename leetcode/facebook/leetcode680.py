class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if the s can be palindrome after deleting at most one character from it.

        Approach:

        This is a simple question. We can iterate with two pointers until we reach a point where
        s[i] != s[j] where i != j.

        At that point, we should split from s[i + 1:j] and s[i:j - 1] and check if these can be palindromes
        if these cannot be palindromes then we should return false otherwise we return true

        :param s:
        :return:
        """
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome(s[i:j]) or self.is_palindrome(
                    s[i + 1 : j + 1]
                )
            i += 1
            j -= 1

        return True

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
