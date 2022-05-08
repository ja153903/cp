from typing import List


def _eval(first: str, second: str, op: str) -> str:
    first_as_int = int(first)
    second_as_int = int(second)

    if op == "+":
        return str(first_as_int + second_as_int)
    elif op == "-":
        return str(first_as_int - second_as_int)
    elif op == "*":
        return str(first_as_int * second_as_int)
    else:
        return str(int(float(first_as_int) / second_as_int))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch in "*+-/":
                second = stack.pop()
                first = stack.pop()

                result = _eval(first, second, ch)
                stack.append(result)
            else:
                stack.append(ch)

        return int(stack[0])
