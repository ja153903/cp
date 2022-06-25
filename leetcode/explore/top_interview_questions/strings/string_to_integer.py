class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0

        while i < len(s) and s[i] == " ":
            i += 1

        is_negative = False
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            is_negative = s[i] == "-"
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result = -result if is_negative else result

        lower_bound = -(2**31)
        upper_bound = 2**31 - 1

        if result < lower_bound:
            return lower_bound

        if result > upper_bound:
            return upper_bound

        return result
