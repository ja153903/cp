from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    """
    This sliding window question solves for finding the longest possible substring of
    similar characters where we can replace at most k characters

    How do we approach this via sliding window?

    What we want to keep track of here is the count of each character.
    We then create a variable called start to keep track of the left pointer
    of our sliding window.
    We also need to keep track of the max count and the max length of any substring.

    In our iteration of the string, we have to make sure we update the count.
    Then we also update the maximum count as we come across. This is a crucial
    step because we want to make sure we optimize for which character we want
    to replace. Intuitively, it makes sense to replace other characters with
    the character that appears the most frequently.

    So after that update, we then check if we need to update our left pointer
    of the sliding window. How we determine this is by checking if the size
    of the current window minus the maximum count of a character is greater
    than k.

    By checking end - start + 1 - max_cnt > k, what we're doing is making sure
    that we're only making at most k replacements. The left side tells us how many
    characters there are in the window that are not the most frequent character.
    So if the value is greater than k, then this means that we have to replace
    more than we are allowed which makes the sliding window invalid

    So in this while loop, we'll have to decrement the count of the character that
    appears in the left pointer of our sliding window and also increasing
    the value of the left pointer.

    Finally, we update the max length if possible with the size of the current
    sliding window.

    :param: s: str ~ the string we're given
    :param: k: int ~ maximum number of replacements
    :return: int ~ length of the longest possible string of similar characters
    """
    counter = defaultdict(int)
    start, max_count, max_len = 0, 0, 0

    for end, ch in enumerate(s):
        counter[ch] += 1
        max_count = max(max_count, counter[ch])

        # size of window - frequency of most frequent char
        # means how many characters there are that are not
        # the most frequent character
        while end - start + 1 - max_count > k:
            counter[s[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len


def minimum_window_substring(s: str, t: str) -> str:
    """
    This is a staple in terms of asking sliding window questions.
    This template here can solve a lot of sliding window problems.

    TODO: Explain this in more detail since this is a fundamental problem

    :param s:
    :param t:
    :return:
    """
    if len(s) < len(t):
        return ""

    counter = defaultdict(int)
    start, min_start, min_len, target = 0, 0, float("inf"), len(t)

    for ch in t:
        counter[ch] += 1

    for end, ch in enumerate(s):
        if counter[ch] > 0:
            target -= 1

        counter[ch] -= 1

        while target == 0:
            current_window_size = end - start + 1
            if current_window_size < min_len:
                min_start = start
                min_len = current_window_size

            counter[s[start]] += 1
            if counter[s[start]] > 0:
                target += 1

            start += 1

    return s[min_start : min_start + min_len] if min_len != float("inf") else ""
