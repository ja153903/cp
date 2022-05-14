from .leetcode355 import Twitter


def test_twitter_flow1():
    twitter = Twitter()

    twitter.postTweet(1, 5)

    assert twitter.getNewsFeed(1) == [5]

    twitter.postTweet(1, 3)
    twitter.postTweet(1, 101)
    twitter.postTweet(1, 13)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 94)
    twitter.postTweet(1, 505)
    twitter.postTweet(1, 333)
    twitter.postTweet(1, 22)
    twitter.postTweet(1, 11)

    assert twitter.getNewsFeed(1) == [11, 22, 333, 505, 94, 2, 10, 13, 101, 3]
