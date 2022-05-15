from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]

        for i in range(1, len(words)):
            if self._is_anagram(words[i], words[i - 1]):
                continue

            result.append(words[i])

        return result

    def _is_anagram(self, a: str, b: str) -> bool:
        a_sorted = "".join(sorted(a))
        b_sorted = "".join(sorted(b))

        return a_sorted == b_sorted
