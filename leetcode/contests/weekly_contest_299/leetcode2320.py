class Solution:
    def countHousePlacements(self, n: int) -> int:
        a, b = 1, 1
        mod = 10**9 + 7

        for _ in range(n):
            a, b = b, (a + b) % mod

        return b * b % mod
