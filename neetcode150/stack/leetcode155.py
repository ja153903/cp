class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return

        _min = self.getMin()
        self.stack.append((val, min(_min, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        top, _ = self.stack[-1]
        return top

    def getMin(self) -> int:
        _, _min = self.stack[-1]
        return _min
