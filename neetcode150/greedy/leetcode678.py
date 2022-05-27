class Solution:
    def checkValidString(self, s: str) -> bool:
        # lo ~ the minimum number of unclosed open parentheses we can have
        # hi ~ the maximum number of unclosed open parentheses we can have
        lo, hi = 0, 0

        for ch in s:
            # if we have an open parenthesis we increment
            if ch == "(":
                hi += 1
                lo += 1
            # if we have a closing parenthesis we decrement
            elif ch == ")":
                hi -= 1
                lo -= 1
            else:
                # if we have a *, we either include the open parenthesis
                # or we include a closing parenthesis
                # lo takes into account the path where we chose a closing parenthesis
                hi += 1
                lo -= 1

            # if the maximum number of unclosed open parentheses is negative, this means we've found
            # an unbalanced string
            if hi < 0:
                return False

            # we want to make sure that minimum number of unclosed parenthesis is never negative
            # we do this because if we allow it to be negative, there can be a case where
            # the lo becomes 0 again even though it might be unbalanced
            # such as example is when s = "(*)(" where lo will end up being 0 if we didn't
            # take the max between lo and 0
            lo = max(lo, 0)

        return lo == 0

    def attempt1(self, s: str) -> bool:
        stack = []
        stars = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append((ch, i))
            elif ch == "*":
                stars.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    # if there is nothing on the stack, we should check if there's anything on stars
                    if not stars:
                        return False

                    stars.pop()

        while stack and stars:
            top, idx = stack.pop()

            if top == "(" and stars[-1] > idx:
                stars.pop()

            if top == ")" and stars[0] < idx:
                stars.pop(0)

        return not stack
