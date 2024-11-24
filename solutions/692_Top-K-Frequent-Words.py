class HeapItem:
    def __init__(self, word, count):
        self.count = count
        self.word = word
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap, res = [], []

        for word, count in count.items():
            heapq.heappush(heap, HeapItem(word, count))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while k:
            res.append(heapq.heappop(heap).word)
            k -= 1
        return list(reversed(res))

        