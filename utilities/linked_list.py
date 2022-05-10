from typing import Optional, List

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


def to_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None

    result = ListNode(0)
    dummy = result

    for item in items:
        dummy.next = ListNode(item)
        dummy = dummy.next

    return result.next


def to_list(node: Optional[ListNode]) -> List[int]:
    if not node:
        return []

    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result
