class Solution:
    def numDecodings(self, s: str) -> int:
        """
        What's the plan here?
        dp[i] ~ number of ways to decode up to index i (not including it)

        dp[0] = 1 ~ there is 1 way to decode an empty string
        dp[1] = 1 if s[0] is between 1 and 9 else 0

        We should add dp[i - 1] to dp[i] if the current string is between 1 and 9.
        We should also add dp[i - 2] to dp[i] if the current string and the previous string is between 10 and 26

        :param s:
        :return:
        """
        n = len(s)

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1 if 1 <= int(s[0]) <= 9 else 0

        for i in range(2, n + 1):
            if 1 <= int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
