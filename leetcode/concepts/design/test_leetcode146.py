from .leetcode146 import LRUCache


def test_lru_cache():
    lru_cache = LRUCache(2)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)

    assert lru_cache.get(1) == 1

    lru_cache.put(3, 3)

    assert lru_cache.get(2) == -1

    lru_cache.put(4, 4)

    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4
