from typing import Optional, List

from data_structures.tree import TreeNode
from utilities.tree import level_order


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        items = level_order(root)
        return [item[-1] for item in items]
