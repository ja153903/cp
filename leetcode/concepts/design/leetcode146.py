from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class LRUCacheNode:
    key: int
    val: int
    next: Optional["LRUCacheNode"] = None
    prev: Optional["LRUCacheNode"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache: Dict[int, LRUCacheNode] = {}
        self.head = LRUCacheNode(0, 0)
        self.tail = LRUCacheNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        node = self._cache[key]

        self._update_lru(node)

        return node.val

    def _update_lru(self, node: LRUCacheNode):
        self._remove_node(node)
        self._move_node_to_head(node)

    def _remove_node(self, node: LRUCacheNode):
        _next = node.next
        _prev = node.prev

        if _prev and _prev.next:
            _prev.next = _next

        if _next and _next.prev:
            _next.prev = _prev

    def _move_node_to_head(self, node: LRUCacheNode):
        _prev = self.head
        _next = self.head.next

        node.prev = _prev
        node.next = _next

        if _prev:
            _prev.next = node
        if _next:
            _next.prev = node

    def put(self, key: int, value: int) -> None:
        at_capacity = len(self._cache) == self.capacity

        if at_capacity and key not in self._cache:
            lru = self._get_lru()
            if lru:
                del self._cache[lru.key]

        if key in self._cache:
            node = self._cache[key]
            node.val = value
        else:
            node = LRUCacheNode(key, value)
            self._cache[key] = node

        self._update_lru(node)

    def _get_lru(self) -> Optional[LRUCacheNode]:
        node = self.tail.prev

        if node:
            self._remove_node(node)

        return node
