class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        a string is good if there are no repeated characters

        given a string s, return the number of good substrings with length 3

        :param s:
        :return:
        """
        if len(s) < 3:
            return 0

        result = 0
        first, second, third = s[0], s[1], s[2]

        if first != second and second != third and first != third:
            result += 1

        for i in range(3, len(s)):
            first, second, third = second, third, s[i]
            if first != second and second != third and first != third:
                result += 1

        return result
