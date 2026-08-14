class Twitter:

    def __init__(self):
        self.recent = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows[userId]:
            self.follows[userId].add(userId)

        self.tweets[userId].append((self.recent, tweetId))
        self.recent -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.follows[userId]:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tw = self.tweets[uid][idx]
                heapq.heappush(heap, (t, tw, uid, idx))
        feed = []

        while heap and len(feed) < 10:
            t, tw, uid, idx = heapq.heappop(heap)
            feed.append(tw)
            if idx - 1 >= 0:
                t2, tw2 = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (t2, tw2, uid, idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
