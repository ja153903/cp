from typing import Optional

from data_structures.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the nth node from the end of the list and return its head.

        Approach:

        1. The brute force approach would be to copy the entire linked list into a list
           and then remove the nth node and reconstruct the linked list with the remaining elements.
           This would run in O(n) time and space.

        2. Another approach would require a bit more thought on how to use fast-slow pointers.

        :param head:
        :param n:
        :return:
        """
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        nums = nums[: len(nums) - n] + nums[len(nums) - n + 1 :]

        root = ListNode(val=0)
        curr = root

        for num in nums:
            curr.next = ListNode(val=num)
            curr = curr.next

        return root.next

    @staticmethod
    def optimize(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0)
        dummy.next = head
        first, second = dummy, dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
