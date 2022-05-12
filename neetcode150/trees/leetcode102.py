from typing import Optional, List

from data_structures.tree import TreeNode
from utilities.tree import level_order


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return level_order(root)
