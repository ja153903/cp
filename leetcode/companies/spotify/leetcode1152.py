from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        by_username = defaultdict(list)
        by_pattern = defaultdict(set)
        data = sorted(
            [(un, ts, wb) for un, ts, wb in zip(username, timestamp, website)],
            key=lambda tup: (tup[0], tup[1]),
        )

        for un, _, wb in data:
            by_username[un].append(wb)

        for un, wbs in by_username.items():
            patterns = combinations(wbs, 3)
            for pattern in patterns:
                key = ",".join(pattern)
                by_pattern[key].add(un)

        _max = 0
        _max_set = []

        for key, value in by_pattern.items():
            length = len(value)
            if length == _max:
                if key < ",".join(_max_set):
                    _max_set = key.split(",")
            elif length > _max:
                _max = len(value)
                _max_set = key.split(",")

        return _max_set
