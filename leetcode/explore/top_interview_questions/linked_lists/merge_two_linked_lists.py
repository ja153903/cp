from typing import Optional

from data_structures.linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, a: Optional[ListNode], b: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not a and not b:
            return None

        if not a:
            return b

        if not b:
            return a

        if a.val < b.val:
            a.next = self.mergeTwoLists(a.next, b)
            return a

        b.next = self.mergeTwoLists(a, b.next)
        return b
