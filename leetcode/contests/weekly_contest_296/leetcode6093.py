class TextEditor:
    """
    There are a couple approaches we can take with this question.

    1. We can use two stacks. for the left partition and for the right partition
    2. Optimize the solution we have now!
    """

    def __init__(self):
        self.cursor_pos = 0
        self.stack = ["|"]

    def addText(self, text: str) -> None:
        if self.cursor_pos == 0:
            self.stack = list(text) + self.stack
            self.cursor_pos += len(text)
        else:
            self.stack = (
                self.stack[: self.cursor_pos]
                + list(text)
                + self.stack[self.cursor_pos :]
            )
            self.cursor_pos += len(text)

    def deleteText(self, k: int) -> int:
        if len(self.stack) == 1 or k == 0:
            return 0

        num_to_delete = min(self.cursor_pos, k)

        if k > self.cursor_pos:
            self.stack = self.stack[self.cursor_pos :]
            self.cursor_pos = 0
        else:
            self.stack = (
                self.stack[: self.cursor_pos - k] + self.stack[self.cursor_pos :]
            )
            self.cursor_pos -= k

        return num_to_delete

    def cursorLeft(self, k: int) -> str:
        if len(self.stack) == 1:
            return ""

        i = self.cursor_pos
        cnt = k

        while i > 0 and cnt > 0:
            self.stack[i], self.stack[i - 1] = self.stack[i - 1], self.stack[i]
            cnt -= 1
            i -= 1

        self.cursor_pos = max(0, self.cursor_pos - k)

        start = max(self.cursor_pos - 10, 0)

        return "".join(self.stack[start : self.cursor_pos])

    def cursorRight(self, k: int) -> str:
        if len(self.stack) == 1:
            return ""

        i = self.cursor_pos
        cnt = k

        while i < len(self.stack) - 1 and cnt > 0:
            self.stack[i], self.stack[i + 1] = self.stack[i + 1], self.stack[i]
            cnt -= 1
            i += 1

        self.cursor_pos = min(self.cursor_pos + k, len(self.stack) - 1)

        start = max(self.cursor_pos - 10, 0)

        return "".join(self.stack[start : self.cursor_pos])
