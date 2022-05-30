from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = Counter(s)

        target = Counter(target)

        result = 0

        while True:
            for ch, count in target.items():
                if counter.get(ch, 0) - count < 0:
                    return result

                if ch in counter:
                    counter[ch] -= count

            result += 1

        return result
