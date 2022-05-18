from collections import deque
from typing import List


ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        """
        Approach:

        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """
        if len(begin_word) != len(end_word):
            return 0

        unique_words = set(word_list)
        queue = deque()

        queue.append((begin_word, 1))

        while queue:
            front, ladder_len = queue.popleft()

            if front == end_word:
                return ladder_len

            if front in unique_words:
                unique_words.remove(front)

            for i in range(len(front)):
                prev = front[:i]
                rest = front[i + 1 :]

                for ch in ALPHABET:
                    word = f"{prev}{ch}{rest}"
                    if word in unique_words:
                        queue.append((word, ladder_len + 1))

        return 0
