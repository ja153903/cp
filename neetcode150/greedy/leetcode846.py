from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], group_size: int) -> bool:
        """
        Alice has some number of cards, and she wants to rearrange the cards into groups so that each group
        is of size groupSize, and consists of groupSize consecutive cards.

        Given an integer array hand where hand[i] is the value written on the ith card and an integer group_size,
        return true if she can rearrange the cards, or false otherwise.

        :param hand:
        :param group_size:
        :return:
        """
        hand.sort()

        counter = Counter(hand)

        for num in hand:
            if counter.get(num) == 0:
                # not a valid starting point
                continue

            start = num

            for _ in range(group_size):
                if counter.get(start, 0) == 0:
                    return False

                counter[start] -= 1
                start += 1

        return True
