from data_structures.trie import Trie as MyTrie


class Trie:
    def __init__(self):
        self._trie = MyTrie()

    def insert(self, word: str) -> None:
        self._trie.insert(word)

    def search(self, word: str) -> bool:
        return self._trie.full_search(word)

    def startsWith(self, word: str) -> bool:
        return self._trie.starts_with(word)
