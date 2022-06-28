import { TreeNode } from "../../data_structures";

function isBalanced(root: TreeNode | null): boolean {
  // how can we tell that a tree is balanced
  function depth(node: TreeNode | null): number {
    if (!node) {
      return 0;
    }

    const left = depth(node.left);
    const right = depth(node.right);

    return Math.max(left, right) + 1;
  }

  if (!root) {
    return true;
  }

  const left = depth(root.left);
  const right = depth(root.right);

  if (Math.abs(left - right) > 1) {
    return false;
  }

  return isBalanced(root.left) && isBalanced(root.right);
}

export default isBalanced;
