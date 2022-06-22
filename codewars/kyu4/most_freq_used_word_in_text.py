from collections import Counter, deque


def top_3_words(text):
    words = deque(text.split(" "))
    sanitized = []

    while words:
        front = words.popleft()
        word = []

        for ch in front:
            if ch.isalpha() or ch == "'":
                word.append(ch.lower())
            else:
                word.append(" ")

        joined = "".join(word)
        _words = joined.split(" ")

        for _word in _words:
            if _word and contains_alpha(_word):
                sanitized.append(_word)

    counter = Counter(sanitized)

    return [word[0] for word in counter.most_common(3)]


def contains_alpha(s):
    for ch in s:
        if ch.isalpha():
            return True

    return False
