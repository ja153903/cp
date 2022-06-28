import { TreeNode } from "../../data_structures";

function diameterOfBinaryTree(root: TreeNode | null): number {
  let maxLength = 0;

  function recurse(node: TreeNode | null): number {
    if (!node) {
      return 0;
    }

    const left = recurse(node.left);
    const right = recurse(node.right);

    maxLength = Math.max(maxLength, left + right);

    return Math.max(left, right) + 1;
  }

  recurse(root);

  return maxLength;
}

export default diameterOfBinaryTree;
