from typing import Optional, List

from data_structures.tree import TreeNode


class Codec:
    SPLITTER = ","
    NULL_NODE = "X"

    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        self._build_string(root, result)
        return "".join(result)

    def _build_string(self, root: Optional[TreeNode], result: List[str]) -> None:
        if not root:
            # if the root is null, then we denote this by the NULL_NODE char and a splitter
            result.append(f"{Codec.NULL_NODE}{Codec.SPLITTER}")
        else:
            # We add to the result list using pre-order traversal
            result.append(f"{root.val}{Codec.SPLITTER}")
            self._build_string(root.left, result)
            self._build_string(root.right, result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(Codec.SPLITTER)
        return self._build_tree(nodes)

    def _build_tree(self, nodes: List[str]) -> Optional[TreeNode]:
        front = nodes.pop(0)

        if front == Codec.NULL_NODE:
            return None
        else:
            node = TreeNode(int(front))
            node.left = self._build_tree(nodes)
            node.right = self._build_tree(nodes)

            return node
