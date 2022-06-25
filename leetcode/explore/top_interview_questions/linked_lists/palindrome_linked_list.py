from typing import Optional

from data_structures.linked_list import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        copy = self.clone(head)
        rev = self.reverse(copy)

        while rev and head:
            if rev.val != head.val:
                return False

            rev = rev.next
            head = head.next

        return True

    def clone(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = ListNode(0)
        runner = copy

        while head:
            runner.next = ListNode(head.val)
            head = head.next
            runner = runner.next

        return copy.next

    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = node

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
