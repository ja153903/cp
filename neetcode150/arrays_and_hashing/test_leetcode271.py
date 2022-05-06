from neetcode150.arrays_and_hashing.leetcode271 import Codec


def test_encode():
    codec = Codec()

    assert codec.encode(["Hello", "World"]) == "5/Hello5/World"
    assert codec.decode("5/Hello5/World") == ["Hello", "World"]
