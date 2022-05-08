from collections import defaultdict


class TimeMap:
    def __init__(self):
        self._map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""

        values = self._map[key]

        left, right = 0, len(values) - 1

        idx = 0

        while left <= right:
            mid = left + (right - left) // 2

            value, current_timestamp = values[mid]

            if current_timestamp <= timestamp:
                idx = mid
                left = mid + 1
            else:
                right = mid - 1

        candidate_value, candidate_timestamp = values[idx]

        return candidate_value if candidate_timestamp <= timestamp else ""
