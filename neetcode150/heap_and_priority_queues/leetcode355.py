import heapq
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Set

from data_structures.priority_queue import PrioritizedItem


@dataclass
class User:
    id: int
    tweets: List[PrioritizedItem] = field(default_factory=list)
    follows: Set[int] = field(default_factory=set)


class Twitter:
    def __init__(self):
        self.users = defaultdict(User)
        self.timestamp = 1

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self._create_user(user_id)

        self.users[user_id].tweets.append(
            PrioritizedItem(priority=self.timestamp, item=tweet_id)
        )

        self._update_timestamp()

    def getNewsFeed(self, user_id: int) -> List[int]:
        if user_id not in self.users:
            return []

        heap = []

        user = self.users[user_id]
        user_tweets = user.tweets

        for tweet in user_tweets:
            heapq.heappush(heap, tweet)
            if len(heap) > 10:
                heapq.heappop(heap)

        follows = user.follows
        for user_id in follows:
            followed_user = self.users[user_id]
            followed_tweets = followed_user.tweets

            for tweet in followed_tweets:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap))

        return [pi.item for pi in result][::-1]

    def follow(self, follower_id: int, followee_id: int) -> None:
        for user_id in [followee_id, follower_id]:
            self._create_user(user_id)

        self.users[follower_id].follows.add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        for user_id in [followee_id, follower_id]:
            self._create_user(user_id)

        if followee_id in self.users[follower_id].follows:
            self.users[follower_id].follows.remove(followee_id)

    def _update_timestamp(self) -> None:
        self.timestamp += 1

    def _create_user(self, user_id: int) -> None:
        if user_id not in self.users:
            self.users[user_id] = User(id=user_id)
