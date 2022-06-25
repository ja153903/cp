from data_structures.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0)

        slow, fast = start, start

        slow.next = head

        # go through first n elements
        for _ in range(n + 1):
            fast = fast.next

        # move the slow pointer until the fast pointer is depleted
        while fast:
            slow = slow.next
            fast = fast.next

        # this removes the nth element
        slow.next = slow.next.next

        return start.next
