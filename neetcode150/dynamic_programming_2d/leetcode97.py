import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @functools.cache
        def _recurse(i: int, j: int, k: int) -> bool:
            if k == len(s3):
                return True

            result = False

            if i < len(s1) and s1[i] == s3[k]:
                result |= _recurse(i + 1, j, k + 1)

            if j < len(s2) and s2[j] == s3[k]:
                result |= _recurse(i, j + 1, k + 1)

            return result

        if len(s1) + len(s2) != len(s3):
            return False

        return _recurse(0, 0, 0)
