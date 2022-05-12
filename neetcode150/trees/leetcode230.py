from typing import Optional

from data_structures.tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # I think we can use an iterative tree traversal here to make sure that
        # we count the kth smallest
        cnt = 0
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            cnt += 1

            if k == cnt:
                return root.val

            root = root.right

        return -1
