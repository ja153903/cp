from collections import defaultdict
from typing import List


class WordDistance:
    def __init__(self, words: List[str]):
        self.mp = defaultdict(list)

        for i, word in enumerate(words):
            self.mp[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1_pos = self.mp.get(word1, [])
        w2_pos = self.mp.get(word2, [])

        result = 3 * 10**4

        i, j = 0, 0

        while i < len(w1_pos) and j < len(w2_pos):
            result = min(result, abs(w1_pos[i] - w2_pos[j]))

            if w1_pos[i] < w2_pos[j]:
                i += 1
            else:
                j += 1

        return result
