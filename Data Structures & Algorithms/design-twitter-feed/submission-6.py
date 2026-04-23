class Twitter:

    def __init__(self):
        self.timer = 0
        self.follow_map = defaultdict(set)
        self.tweets_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_map[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user_ids = [userId] + list(self.follow_map[userId])

        all_tweets = []
        for user_id in user_ids:
            user_tweets = self.tweets_map[user_id]
            all_tweets.extend(user_tweets[-10:])
        
        heapq.heapify(all_tweets)

        res = []
        # while len(all_tweets) > 0 and count < 10:
        while all_tweets and len(res) < 10:
            res.append(heapq.heappop(all_tweets)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follow_map[followerId].discard(followeeId)
        