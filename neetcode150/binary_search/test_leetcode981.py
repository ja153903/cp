from neetcode150.binary_search.leetcode981 import TimeMap


def test_time_map():
    tmap = TimeMap()

    tmap.set("foo", "bar", 1)
    assert tmap.get("foo", 1) == "bar"
    assert tmap.get("foo", 3) == "bar"
    tmap.set("foo", "bar2", 4)
    assert tmap.get("foo", 4) == "bar2"
    assert tmap.get("foo", 5) == "bar2"
