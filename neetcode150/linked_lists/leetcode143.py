from typing import Optional

from data_structures.linked_list import ListNode
from utilities.linked_list import reverse


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # now we have slow at half
        half = slow.next
        if slow.next:
            slow.next = None

        reversed_head = reverse(half)
        curr = head

        while curr:
            _next = curr.next
            curr.next = reversed_head
            reversed_head = _next

            curr = curr.next

        return head
