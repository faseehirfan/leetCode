class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            euclid = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-euclid, (x,y)))
            if len(heap) > k:
                heapq.heappop(heap)

        return [cords for _, cords in heap] 