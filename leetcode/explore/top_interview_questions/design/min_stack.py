class MinStack:
    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append((val, val))
        else:
            _min = min(self.getMin(), val)
            self._stack.append((val, _min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        _top = self._stack[-1]

        return _top[0]

    def getMin(self) -> int:
        _top = self._stack[-1]

        return _top[1]
