class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        
        while len(stones) > 1:
            s1 = heappop(stones)
            s2 = heappop(stones)
            if s1 != s2:
                heappush(stones, s1 - s2)
        return -stones[0] if len(stones) > 0 else 0
            
s