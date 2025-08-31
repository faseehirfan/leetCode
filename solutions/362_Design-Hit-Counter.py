class HitCounter:

    def __init__(self):
        self.hits = []
        self.lookback = 300

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        cutoff = bisect_right(self.hits, timestamp - self.lookback)
        self.hits = self.hits[cutoff:]
        return len(self.hits)
 


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)