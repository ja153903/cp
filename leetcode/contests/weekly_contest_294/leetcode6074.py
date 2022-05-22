from collections import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)

        counter = Counter(s)

        if letter not in counter:
            return 0

        return int(counter.get(letter) / n * 100)
