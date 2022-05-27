from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """

        :param triplets:
        :param target:
        :return:
        """
        # filter out items that are above the target
        filtered = []

        for a, b, c in triplets:
            ta, tb, tc = target

            if a > ta or b > tb or c > tc:
                continue

            filtered.append((a, b, c))

        if not filtered:
            return False

        start = 0

        while start <= len(filtered) - 1:
            front = filtered[start]
            back = filtered[-1]

            filtered[-1] = (
                max(front[0], back[0]),
                max(front[1], back[1]),
                max(front[2], back[2]),
            )

            if (
                filtered[-1][0] == target[0]
                and filtered[-1][1] == target[1]
                and filtered[-1][2] == target[2]
            ):
                return True

            start += 1

        return False
