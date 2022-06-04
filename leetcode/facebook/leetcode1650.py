class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        """
        Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

        According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a
        tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant
        of itself)."

        Approach:

        This problem is similar to that linked list problem that requires us to find the convergence
        point of two linked lists. In this case, we want to find the convergence point of two nodes
        going up its parent. This is something good to think about since both nodes are essentially
        just going in a straight line, if we iterate twice to the root, we'll know if it converges at
        any point.

        :param p:
        :param q:
        :return:
        """
        p1, p2 = p, q

        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1
