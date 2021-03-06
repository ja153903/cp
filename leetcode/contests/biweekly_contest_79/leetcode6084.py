from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        log = defaultdict(int)

        for msg, sender in zip(messages, senders):
            log[sender] += len(msg.split(" "))

        _max = (None, 0)

        for sender, word_count in log.items():
            max_sender, max_count = _max

            if (
                max_sender is None
                or (max_count == word_count and max_sender < sender)
                or (word_count > max_count)
            ):
                _max = (sender, word_count)

        return _max[0] if _max[0] is not None else ""
