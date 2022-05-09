import heapq
from typing import List, Optional

from data_structures.linked_list import ListNode
from data_structures.priority_queue import PrioritizedItem


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode(0)
        dummy = result
        heap = []

        for item in lists:
            if item:
                heapq.heappush(heap, PrioritizedItem(item.val, item))

        while heap:
            pitem = heapq.heappop(heap)
            node = pitem.item

            dummy.next = ListNode(node.val)
            dummy = dummy.next

            if node.next:
                heapq.heappush(heap, PrioritizedItem(node.next.val, node.next))

        return result.next
