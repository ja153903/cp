from typing import Optional

from data_structures.linked_list import RandomNode as Node


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        copies = {None: None}

        curr = head

        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]

            curr = curr.next

        return copies[head]
