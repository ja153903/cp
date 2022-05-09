from typing import Optional

from data_structures.linked_list import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode(0)
        itr = result

        carry = 0

        while l1 or l2:
            current = carry

            if l1:
                current += l1.val
                l1 = l1.next

            if l2:
                current += l2.val
                l2 = l2.next

            itr.next = ListNode(current % 10)
            itr = itr.next
            carry = current // 10

        if carry:
            itr.next = ListNode(carry)

        return result.next
