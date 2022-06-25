from typing import Optional

from data_structures.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next if slow else None
            fast = fast.next.next

            if slow == fast:
                return True

        return False
