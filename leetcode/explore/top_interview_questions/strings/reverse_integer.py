class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = -x if is_negative else x
        rev = int("".join(list(str(x))[::-1]))

        if rev >= 2**31:
            return 0

        return rev if not is_negative else -rev
