from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)

        for i in range(len(num)):
            if counter[str(i)] != int(num[i]):
                return False

        return True
