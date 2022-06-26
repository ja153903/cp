from typing import List


class Solution:
    def maxScore(self, card_points: List[int], k: int) -> int:
        n = len(card_points)
        if k >= n:
            return sum(card_points)

        forward = []

        for i in range(k):
            if not forward:
                forward.append(card_points[i])
            else:
                forward.append(forward[-1] + card_points[i])

        backward = []

        for i in range(n - 1, n - 1 - k, -1):
            if not backward:
                backward.append(card_points[i])
            else:
                backward.append(backward[-1] + card_points[i])

        current_max = max(forward[-1], backward[-1])

        i, j = 0, k - 2

        while i < k - 1 and j >= 0:
            current_max = max(current_max, forward[i] + backward[j])
            i += 1
            j -= 1

        return current_max
