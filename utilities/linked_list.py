from typing import Optional

from data_structures.linked_list import ListNode


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    curr, prev = head, None

    while curr:
        _next = curr.next
        curr.next = prev
        prev = curr
        curr = _next

    return prev


def find_middle_of_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    slow, fast = head, head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow.next
