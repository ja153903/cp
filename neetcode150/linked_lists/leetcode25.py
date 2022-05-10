from typing import Optional

from data_structures.linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

        k is a positive integer and is less than or equal to the length of the linked list.
        If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

        You may not alter the values in the list's nodes, only nodes themselves may be changed.

        :param head:
        :param k:
        :return:
        """
        if not head:
            return None

        end, begin = head, head

        for _ in range(k):
            try:
                end = end.next
            except AttributeError:
                return head

        prev, curr = None, begin

        while curr != end:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        runner = prev

        while runner.next:
            runner = runner.next

        runner.next = self.reverseKGroup(end, k)

        return prev
