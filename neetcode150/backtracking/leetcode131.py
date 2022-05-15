from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Given a string s, partition s such that every substring of the partition is a palindrome.
        Return all possible palindrome partitioning of s.

        A palindrome string is a string that reads the same backward as forward.

        We can start a path for each character.
        At each step, we can do one of two things:
        1. concatenate string
        2. check if current path itself can be a palindrome then add next character as new string

        :param s:
        :return:
        """
        result = []

        self._backtrack(s, result, [], 0)

        return result

    def _backtrack(self, s: str, result: List[List[str]], path: List[str], start: int):
        if len(s) == start:
            for p in path:
                if not self._is_palindrome(p):
                    return

            result.append(list(path))
        else:
            ch = s[start]

            if not path:
                self._backtrack(s, result, path + [ch], start + 1)
            else:
                # check if last item in path is a palindrome
                is_last_item_palindrome = self._is_palindrome(path[-1])

                if is_last_item_palindrome:
                    self._backtrack(s, result, path + [ch], start + 1)

                tmp = path[-1]
                path[-1] = f"{path[-1]}{ch}"
                self._backtrack(s, result, path, start + 1)
                path[-1] = tmp

    @staticmethod
    def _is_palindrome(s: str) -> bool:
        return s == s[::-1]
