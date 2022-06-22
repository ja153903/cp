from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        # at most will size elements in the queue
        self._capacity = size
        self._queue = deque()
        self._sum = 0

    def next(self, val: int) -> float:
        if len(self._queue) >= self._capacity:
            front = self._queue.popleft()
            self._sum -= front

        self._sum += val
        self._queue.append(val)

        return self._sum / len(self._queue)
