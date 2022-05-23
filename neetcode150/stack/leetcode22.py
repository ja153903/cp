from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        To use a stack with this, we essentially perform some sort of BFS

        :param n:
        :return:
        """
        result = []
        stack = [("(", 1, 0)]

        while stack:
            cur, opn, close = stack.pop()
            if opn < close or opn > n or close > n:
                continue

            if opn == n and close == n:
                result.append(cur)

            stack.append((cur + "(", opn + 1, close))
            stack.append((cur + ")", opn, close + 1))

        return result
