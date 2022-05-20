class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        """
        We can keep track of this in a dp matrix

        dp[i][j] ~ the longest common subsequence up to index i of s and index j of t

        We increase dp[i][j] if the characters are the same else.
        Otherwise we get the max from dp[i - 1][j] and dp[i][j - 1]

        :param s:
        :param t:
        :return:
        """
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(s)][len(t)]

    def recursion(self, s: str, t: str) -> int:
        """
        If the characters are the same, then we move the pointer forward for both of them.
        Otherwise we take the max of moving one of the pointers
        :param s:
        :param t:
        :return:
        """

        def _recurse(i: int, j: int) -> int:
            if len(s) == i or len(t) == j:
                return 0

            if s[i] == t[j]:
                # increment both if the characters are the same
                return 1 + _recurse(i + 1, j + 1)

            return max(_recurse(i, j + 1), _recurse(i + 1, j))

        return _recurse(0, 0)
