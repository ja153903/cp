def solution(array_a, array_b):
    result = 0
    count = 0

    for a, b in zip(array_a, array_b):
        result += abs(a - b) ** 2
        count += 1

    return result / count if count > 0 else 0
