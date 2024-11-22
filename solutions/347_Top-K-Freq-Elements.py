class Solution:
    # O(n) time, O(n) space, bucket sort approach
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        count = [[] for _ in range(len(nums) + 1)] 
        res = []

        for key, val in freq.items():
            count[val].append(key)

        for n in reversed(count):
            res.extend(n)
            if len(res) == k:
                return res

    # O(klogn) time, O(n) space, max heap approach
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_heap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(max_heap)
        res = []

        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res


    # O(nlogk) time, O(n) space, min heap approach
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [key for _, key in heap] 