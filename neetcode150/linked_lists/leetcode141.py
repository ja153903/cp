from typing import Optional

from data_structures.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast, slow = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
