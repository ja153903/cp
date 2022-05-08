from typing import List


def can_finish(piles: List[int], k: int, h: int) -> bool:
    hours_needed = 0

    for pile in piles:
        hours_needed += pile // k
        if pile % k > 0:
            hours_needed += 1

    return hours_needed <= h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
        The guards have gone and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
        and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
        and will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

        Return the minimum integer k such that she can eat all the bananas within h hours.

        Approach:

        Given that we need to decide a k such that we can finish all the items within h hours.
        We can iterate from min_pile to max_pile

        :param piles:
        :param h:
        :return:
        """
        min_pile, max_pile = 1, max(piles)
        k = max_pile

        while min_pile <= max_pile:
            mid_pile = min_pile + (max_pile - min_pile) // 2

            # Create a function here to determine if we're able to finish
            # within the time the guards get here
            if can_finish(piles, mid_pile, h):
                k = min(k, mid_pile)
                max_pile = mid_pile - 1
            else:
                min_pile = mid_pile + 1

        return k
