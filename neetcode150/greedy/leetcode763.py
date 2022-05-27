from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        You are given a string s. We want to partition the string into as many parts as possible so that each letter
        appears in at most one part.

        Note that the partition is done so that after concatenating all the parts in order,
        the resultant string should be s.

        Return a list of integers representing the size of these parts.

        :param s:
        :return:
        """
        pos = {}

        for i, ch in enumerate(s):
            pos[ch] = i

        result = []
        start, reach = 0, 0

        for i, ch in enumerate(s):
            reach = max(reach, pos[ch])

            if i == reach:
                result.append(reach - start + 1)
                start = i + 1

        return result
