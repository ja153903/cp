from data_structures.trie import TrieNode


class WordDictionary:
    """
    Approach:
    This is a typical Trie problem.
    The addWord functionality will work by inserting items into the Trie.
    The only part we really have to take care of here is the search.
    Notice that whenever there is a dot, we have to iterate over every possible character
    at that level of the TrieNode.
    """

    def __init__(self):
        self._root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self._root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]

        current.has_word = True

    def search(self, word: str) -> bool:
        return self.dfs(self._root, word, 0)

    def dfs(self, current: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            return current.has_word

        ch = word[index]

        if ch != ".":
            if ch not in current.children:
                return False

            return self.dfs(current.children[ch], word, index + 1)

        for key, value in current.children.items():
            if self.dfs(value, word, index + 1):
                return True

        return False
