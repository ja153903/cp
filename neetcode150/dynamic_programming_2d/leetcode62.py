import functools


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # let dp[i][j] be the number of paths from the top left to the coordinates i, j
        for i in range(n):
            dp[0][i] = 1

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

    def recursion(self, m: int, n: int) -> int:
        """
        To identify a path from (0, 0) to (m - 1, n - 1),
        we should return 1 if we've reached that point
        if we end up hitting a point we've visited before,
        then we should reach back to see what type of value we
        got there.

        :param m:
        :param n:
        :return:
        """

        @functools.cache
        def recurse(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0

            return recurse(i - 1, j) + recurse(i, j - 1)

        return recurse(m - 1, n - 1)
