from data_structures.linked_list import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Given that this is a singly linked list, we can't use some scheme
        with a prev node.

        What we can do is make sure that the node we're given has the information
        from the next node.
        """
        if node:
            node.val = node.next.val
            node.next = node.next.next
