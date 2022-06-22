def get_count(sentence):
    count = 0

    for ch in sentence:
        if ch in "aeiou":
            count += 1

    return count
