from dataclasses import dataclass
from typing import Optional


@dataclass
class DoublyLinkedList:
    key: int
    val: int
    next: Optional["DoublyLinkedList"] = None
    prev: Optional["DoublyLinkedList"] = None


class LRUCache:
    """
    The idea with this problem is to create a doubly linked list.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyLinkedList(0, 0)
        self.tail = DoublyLinkedList(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.move_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.move_to_head(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                lru = self.lru
                self.remove_node(lru)
                del self.cache[lru.key]

            node = DoublyLinkedList(key=key, val=value)

            self.add_to_head(node)

            self.cache[key] = node

    def move_to_head(self, node: DoublyLinkedList) -> None:
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node: DoublyLinkedList) -> None:
        prev = node.prev
        next = node.next

        if prev:
            prev.next = next

        if next:
            next.prev = prev

    def add_to_head(self, node: DoublyLinkedList) -> None:
        prev = self.head
        next = self.head.next

        node.prev = prev
        node.next = next

        prev.next = node
        next.prev = node

    @property
    def lru(self):
        return self.tail.prev
