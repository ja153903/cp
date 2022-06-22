from collections import Counter


def anagrams(word, words):
    word_counter = Counter(word)
    result = []

    for _word in words:
        if word_counter == Counter(_word):
            result.append(_word)

    return result
