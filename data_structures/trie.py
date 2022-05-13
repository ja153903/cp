from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict, Callable


@dataclass
class TrieNode:
    has_word: bool = False
    children: DefaultDict[str, "TrieNode"] = field(default_factory=defaultdict)


class Trie:
    def __init__(self):
        self._root = TrieNode()

    @property
    def root(self):
        return self._root

    def insert(self, word: str) -> None:
        current = self._root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]

        current.has_word = True

    def full_search(self, word: str) -> bool:
        return self._search(word, lambda node: node.has_word)

    def starts_with(self, prefix: str) -> bool:
        return self._search(prefix, lambda _: True)

    def _search(self, word: str, func: Callable[[TrieNode], bool]) -> bool:
        current = self._root

        for ch in word:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return func(current)
