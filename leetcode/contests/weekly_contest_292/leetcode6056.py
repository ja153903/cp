class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        You are given a string num representing a large integer.
        An integer is good if it meets the following conditions:
            * It is a substring of num with length 3.
            * It consists of only one unique digit.
            * Return the maximum good integer as a string or an empty string "" if no such integer exists.

        A substring is a contiguous sequence of characters within a string.
        There may be leading zeroes in num or a good integer.

        Approach:
        We can brute force this problem given that constraints are small.
        What we want to do is find all substrings of length 3 that are unique
        :param num:
        :return:
        """
        result = set()

        for i in range(len(num) - 2):
            if len(set(num[i : i + 3])) == 1:
                result.add(num[i : i + 3])

        return max(result, key=lambda s: int(s)) if result else ""
