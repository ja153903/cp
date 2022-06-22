class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        We don't want to remove an item if we don't need to.
        The only ones we really want to remove are parenthesis
        that don't have a matching pair.

        Suppose we have a string like "lee(t))"
        What we can do is ignore any alphabetic characters and only focus on parenthesis
        Whenever we find an open parenthesis, we add its index to a stack and mark it on another stack
        as an empty character. Then, if we find a corresponding closing parenthesis, we can remove the top of the stack.
        and place the parenthesis where we need it.

        If we find a closing parenthesis with no matching opening parenthesis, this means that we don't want to add
        this closing parenthesis, so we skip it.

        My solution here is O(n) time and space

        :param s:
        :return:
        """
        parenthesis_stack = []
        result = []

        for i, ch in enumerate(s):
            if ch.isalpha():
                result.append(ch)
            elif ch == "(":
                parenthesis_stack.append(i)
                result.append("")
            elif ch == ")":
                if not parenthesis_stack:
                    result.append("")
                else:
                    idx = parenthesis_stack.pop()
                    result[idx] = "("
                    result.append(")")

        return "".join(result)
